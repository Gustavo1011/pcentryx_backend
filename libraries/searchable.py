''' Librería de funciones con ElasticSearch '''
from datetime import datetime
from flask import current_app

def add_to_index(doc_type, model):
    ''' Añade documento al índice '''
    if not current_app.elasticsearch:
        return
    index = current_app.config['ELASTICSEARCH_INDEX'] + "_" + doc_type
    exist_index = current_app.elasticsearch.indices.exists(index=index)
    if exist_index is False:
        create_index(index)
    exist_doc_type = current_app.elasticsearch.indices.exists_type(index=index, doc_type=index)
    if exist_doc_type is False:
        properties = {}
        for field in model.__mapping__:
            if model.__mapping__[field]['type'] != 'array':
                properties[field] = model.__mapping__[field]
        body = {
            'properties': properties
        }
        current_app.elasticsearch.indices.put_mapping(index, body, index=index)
    payload = {}
    for field in model.__mapping__:
        payload[field] = getattr(model, field)
        if isinstance(payload[field], datetime):
            payload[field] = str(payload[field].strftime("%Y-%m-%d %H:%M:%S"))

    refresh = "wait_for"
    if current_app.config['ELASTICSEARCH_REFRESH'] == "false" or \
    (hasattr(model, 'cascade_searchable') and getattr(model, 'cascade_searchable')):
        refresh = "false"
    current_app.elasticsearch.index(
        index=index,
        id=model.id,
        body=payload,
        doc_type=index,
        refresh=refresh
    )

def remove_from_index(doc_type, model):
    ''' Remueve documento del índice '''
    if not current_app.elasticsearch:
        return
    index = current_app.config['ELASTICSEARCH_INDEX'] + "_" + doc_type
    current_app.elasticsearch.delete(index=index, id=model.id, doc_type=index)

def clear_doc_type(doc_type):
    ''' Limpia el tipo de documento '''
    if not current_app.elasticsearch:
        return
    index = current_app.config['ELASTICSEARCH_INDEX'] + "_" + doc_type
    exist_index = current_app.elasticsearch.indices.exists(index=index)
    if exist_index is False:
        return
    body = {"query": {"match_all": {}}}
    current_app.elasticsearch.delete_by_query(index, body, doc_type=index)

def create_index(index):
    '''Crea índice de ElasticSearch'''
    body = {
        'settings': {
            'number_of_shards': 3,
            'number_of_replicas': 2,
            'blocks': {
                'read_only_allow_delete': False
            },
            "analysis": {
                "tokenizer" : {
                    "comma" : {
                        "type" : "pattern",
                        "pattern" : ","
                    }
                },
                "normalizer" : {
                    "lowercase_normalizer" : {
                        "filter" : [
                            "lowercase", "asciifolding"
                        ],
                        "type" : "custom",
                        "char_filter" : []
                    }
                },
                "analyzer" : {
                    "comma" : {
                        "type" : "custom",
                        "tokenizer" : "comma"
                    }
                }
            }
        }
    }
    current_app.elasticsearch.indices.create(index, body=body)

# pylint: disable=line-too-long, too-many-locals, too-many-branches, too-many-arguments, too-many-statements
def query_index(doc_type, queries, offset, limit, sort, order=None):
    ''' Búsqueda de documentos de índice '''
    if not current_app.elasticsearch:
        return [], 0
    index = current_app.config['ELASTICSEARCH_INDEX'] + "_" + doc_type
    if not current_app.elasticsearch.indices.exists(index):
        return [], 0
    if offset and limit:
        if int(limit) > 10000:
            limit = 10000
        if (int(offset) - 1) * int(limit) > 10000:
            offset = 10000 / int(limit)
    query = {"match_all": {}}
    if queries:
        query = {'bool': {'must': [], 'must_not': []}}
        filter_function = 'def arreglo_1 = []; def arreglo_2 = []; def is_valid = true;'
        for _query in queries:
            if _query["type"] == 'match':
                query["bool"]["must"].append({"term": {_query["field"]: _query["value"]}})

            if _query["type"] == 'not_match':
                query["bool"]["must_not"].append({"term": {_query["field"]: _query["value"]}})

            if _query["type"] == 'exists':
                query["bool"]["must"].append({"exists": {"field": _query["field"]}})

            if _query["type"] == 'not_exists':
                query["bool"]["must_not"].append({"exists": {"field": _query["field"]}})

            if _query["type"] == 'like':
                query["bool"]["must"].append({"wildcard": {_query["field"]: _query["value"]}})

            if _query["type"] == 'or_multiple_match':
                _bool = {"bool": {"should": []}}
                for _field in _query["fields"]:
                    _bool["bool"]["should"].append({"term": {_field: _query["value"]}})
                query["bool"]["must"].append(_bool)

            if _query["type"] == 'or_multiple_values':
                _bool = {"bool": {"should": []}}
                for _value in _query["values"]:
                    _bool["bool"]["should"].append({"term": {_query["field"]: _value}})
                query["bool"]["must"].append(_bool)

            if _query["type"] == 'or_multiple_like':
                _bool = {"bool": {"should": []}}
                for _field in _query["fields"]:
                    _bool["bool"]["should"].append({"wildcard": {_field: _query["value"]}})
                query["bool"]["must"].append(_bool)

            if _query["type"] == 'date_range':
                exists_field = False
                for sub_query in query["bool"]["must"]:
                    if 'range' in sub_query and _query["field"] in sub_query['range']:
                        exists_field = True
                        sub_query['range'][_query["field"]][_query["date_math"]] = _query["value"]
                if exists_field is False:
                    query["bool"]["must"].append({
                        "range": {
                            _query["field"]: {
                                _query["date_math"]: _query["value"]
                            }
                        }
                    })
            if _query["type"] == 'query':
                query["bool"]["must"].append(_query["query"])

            if _query["type"] == 'compare_arrays_or':
                filter_function += 'arreglo_1 = doc["' + _query["field"] + '"];' + \
                                    'arreglo_2 = ' + str(_query["value"]) + ';' + \
                                    """ is_valid = false;
                                        for(def i = 0; i<arreglo_2.length; i++){
                                            def flag = false;
                                            for(def j=0; j<arreglo_1.length;j++){
                                                if(arreglo_2[i]==arreglo_1[j]){
                                                    flag=true;
                                                    break;
                                                }
                                            }
                                            if(flag==true){
                                                is_valid = true;
                                                break;
                                            }
                                        }
                                        if (is_valid == false){
                                            return false;
                                        }
                                   """

            if _query["type"] == 'compare_arrays_and':
                filter_function += 'arreglo_1 = doc["' + _query["field"] + '"];' + \
                                    'arreglo_2 = ' + str(_query["value"]) + ';' + \
                                    """ is_valid = true;
                                        for(def i = 0; i<arreglo_2.length; i++){
                                            def flag = false;
                                            for(def j=0; j<arreglo_1.length;j++){
                                                if(arreglo_2[i]==arreglo_1[j]){
                                                    flag=true;
                                                    break;
                                                }
                                            }
                                            if(flag==false){
                                                is_valid = false;
                                                break;
                                            }
                                        }
                                        if (is_valid == false){
                                            return false;
                                        }
                                   """
        if filter_function != 'def arreglo_1 = []; def arreglo_2 = []; def is_valid = true;':
            filter_function += 'return true;'
            query["bool"]["must"].append({"script": {"script": {
                "source": filter_function,
                "lang": "painless"
            }}})

    request_count = current_app.elasticsearch.count(
        index=index, doc_type=index, body={'query': query})
    if offset and limit:
        body_dictionary = {'query': query, 'from': (offset - 1) * limit, 'size': limit}
    else:
        body_dictionary = {'query': query, 'size': 10000}

    if order is None and isinstance(sort, dict):
        search = current_app.elasticsearch.search(
            index=index, doc_type=index,
            body={
                **body_dictionary,
                "sort" : {
                    "_script" : {
                        "type" : sort['type'],
                        "script" : {
                            "lang": "painless",
                            "source": sort['source']
                        },
                        "order" : sort['order']
                    }
                }
            }
        )
    else:
        order_by = "%s:%s" % (sort, order)
        search = current_app.elasticsearch.search(
            index=index, doc_type=index,
            body=body_dictionary,
            sort=order_by
        )
    ids = [int(hit['_id']) for hit in search['hits']['hits']]
    return ids, request_count['count']
