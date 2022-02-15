"""
document_interface.py: Interface to generate documents
"""
import time
from behave import given

@given('Importing document')
def importing_document(context):
    """ Importa un documento """
    context.execute_steps("""
        Given Integrating login module
        And Preparing valid data document
        When Creating document
        Then Satisfactory response 201
        And Saving document in global
    """)
    time.sleep(2)

@given('Importing document with due_date')
def importing_document_with_due_date(context):
    """ Importa un documento con fecha final """
    context.execute_steps("""
        Given Integrating login module
        And Preparing valid data document
        And Adding dated 15 days ago issue_date in data
        And Adding dated after 15 days due_date in data
        When Creating document
        Then Satisfactory response 201
        And Saving document in global
    """)
    time.sleep(2)

@given('Importing expired document')
def importing_expired_document(context):
    """ Importa un documento con fecha final expirada """
    context.execute_steps("""
        Given Integrating login module
        And Preparing valid data document
        And Adding dated 45 days ago issue_date in data
        And Adding dated 15 days ago due_date in data
        When Creating document
        Then Satisfactory response 201
        And Saving document in global
    """)
    time.sleep(2)

# Especificaciones de Documento 004
# - Tipo de autorizacion: 2 -> Licencia
# - Pais: 1 -> Costa Rica
# - Tipos de categorias: Importacion(1) y transporte(3)
# - Numero de archivos: 1
# - Es un documento activo y no tiene fecha de vencimiento
@given('Importing document 004')
def import_document_004(context):
    """ Importa un documento con las especificaciones indicadas """
    context.execute_steps("""
        Given Integrating login module
        And Preparing valid data document
        And Adding data of document 004
        When Creating document
        Then Satisfactory response 201
        And Saving document in global
    """)
    time.sleep(2)

# Especificaciones de Documento 005
# - Tipo de autorizacion: 2 -> Licencia
# - Pais: 1 -> Costa Rica
# - Tipos de categorias: Almacenaje(4) y Precursor(6)
# - Numero de archivos: 1
# - Es un documento activo y no tiene fecha de vencimiento
@given('Importing document 005')
def import_document_005(context):
    """ Importa un documento con las especificaciones indicadas """
    context.execute_steps("""
        Given Integrating login module
        And Preparing valid data document
        And Adding data of document 005
        When Creating document
        Then Satisfactory response 201
        And Saving document in global
    """)
    time.sleep(2)

@given('Deleting documents of global')
def deleting_documents_of_global(context):
    """ Elimina todos los documentos registrados en el global """
    count_documents = context.global_count('document')
    if count_documents is not None:
        for _ in range(count_documents):
            context.execute_steps("""
                Given Integrating login module
                And Adding id in url for document
                When Deleting document
                Then Satisfactory response 200
                And Removing document of global
            """)

@given('Importing deleted document')
def importing_deleted_document(context):
    """ Importa un documento eliminado """
    context.execute_steps("""
        Given Importing document
        And Integrating login module
        And Adding id in url for document
        And Preparing valid data for delete
        When Deleting document
        Then Satisfactory response 200
    """)
    time.sleep(2)

@given('Renewing document getting global')
def renewing_document_getting_global(context):
    """ Renueva un documento obteniendo el id de la variable global """
    context.execute_steps("""
        Given Integrating login module
        And Preparing pre data from document expired
        And Preparing data for renew document
        And Removing field due_date in data
        When Renewing permission
        Then Satisfactory response 200
        And Saving document in global
    """)
    time.sleep(2)

@given('Deleting document getting global')
def deleting_document_getting_global(context):
    """ Elimine un documento obteniendo el id de la variable global """
    context.execute_steps("""
        Given Integrating login module
        And Adding id in url for document
        And Preparing valid data for delete
        When Deleting document
        Then Satisfactory response 200
        And Checking document history for the deleted
        And Saving document in global
    """)
    time.sleep(2)

@given('Updating document getting global')
def updating_document_getting_global(context):
    """ Edita un documento obteniendo el id de la variable global """
    context.execute_steps("""
        Given Integrating login module
        And Preparing data for update document
        When Updating permission
        Then Satisfactory response 200
        And Saving document in global
    """)
    time.sleep(2)
