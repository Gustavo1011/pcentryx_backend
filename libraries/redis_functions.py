''' Librería de funciones para Redis '''

import os

def delete_cascade(entity):
    ''' Método para correr comando para iniciar borrado a cascada '''
    os.system("flask model_base cascade_delete {}".format(str(entity)))

def null_entity(entity):
    ''' Método para correr comando para establecer nulo la relación de entidad '''
    os.system("flask model_base null_entity {}".format(str(entity)))

def update_stock_from_requisition(data):
    ''' Método para correr comando para actualizar stock de producto desde requisición '''
    os.system("flask stock_movement update_stock_from_requisition -- {} {} {} {} {} {} {}".format(
        str(data['type_action']),
        str(data['code']),
        str(data['user_id']),
        str(data['company_id']),
        str(data['product_id']),
        str(data['field']),
        str(data['amount'])
    ))
