rules = {
    'document_id': [
        {
            'rule': 'exist',
            'field': 'id',
            'model': 'Document',
            'message': 'The document was not found'
        }
    ],
    'id': [
        {
            'rule': 'exist',
            'field': 'id',
            'model': 'Document',
            'message': 'The document was not found'
        }
    ],
    'country_id': [
        {
            'rule': 'exist',
            'field': 'id',
            'model': 'Country',
            'message': 'The country was not found'
        }
    ],
    'product_id': [
        {
            'rule': 'exist',
            'field': 'id',
            'model': 'Product',
            'message': 'The product was not found'
        }
    ],
    'type_document_authorization_id': [
        {
            'rule': 'exist',
            'field': 'id',
            'model': 'TypeDocumentAuthorization',
            'message': 'The type document authorization was not found'
        }
    ],
    'type_document_categories': [
        {
            'rule': 'no_repeat_in_array',
            'of_field': 'value',
            'message': 'ID should not be repeated'
        },
        {
            'rule': 'exist_in_array',
            'field': 'id',
            'model': 'TypeDocumentCategory',
            'of_field': 'value',
            'message': 'The type document category was not found'
        }
    ]
}
