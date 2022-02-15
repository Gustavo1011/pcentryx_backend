"""
product_inteface.py: Interface to generate products
"""
import time
from behave import given # pylint: disable=import-error

# Especificaciones de producto 001 (Solo paso 1)
# - Tipo de producto: Equipo
# - Tipo de comunicacion: Manual y MTR
# - Subcategoria: Subcategoria 001
# - Categoria: Categoria 001
# - Marca: 1
# - Estado: Activo
# - Cuenta con data en todos los campos opcionales
@given('Importing product 001 step 01')
def importing_product_001_step_01(context):
    """ Importa un producto """
    context.execute_steps("""
        Given Importing brand
        Given Importing subcategory
        And Integrating login module
        And Preparing data for create general product information
        When Saving general product information
        Then Satisfactory response 200
        And Saving product in global
    """)
    time.sleep(2)

# Especificaciones de producto 001 (Hasta el paso 2)
# - Tipo de producto: Equipo
# - Tipo de comunicacion: Manual y MTR
# - Subcategoria: Subcategoria 001
# - Categoria: Categoria 001
# - Marca: Marca 001
# - Estado: Activo
# - Cuenta con data en todos los campos opcionales
# ----
# - Todos los transportes habilitados
# - Temperatura: 20 - 100
# - Producto no relacionado: 2
@given('Importing product 001 step 02')
def importing_product_001_step_02(context):
    """ Importa un producto """
    context.execute_steps("""
        Given Importing product 001 step 01
        And Integrating login module
        And Preparing data for create product standard
        When Saving product standard
        Then Satisfactory response 200
    """)
    time.sleep(2)

# Especificaciones de producto 001 (Completo)
# - Tipo de producto: Equipo
# - Tipo de comunicacion: Manual y MTR
# - Subcategoria: Subcategoria 001
# - Categoria: Categoria 001
# - Marca: Marca 001
# - Estado: Activo
# - Cuenta con data en todos los campos opcionales
# ----
# - Todos los transportes habilitados
# - Temperatura: 20 - 100
# - Producto no relacionado: 2
@given('Importing product 001')
def importing_product_001(context):
    """ Importa un producto """
    context.execute_steps("""
        Given Importing product 001 step 02
        And Importing document 004
        And Integrating login module
        And Preparing data for save availability document product
        When Saving availability document product
        Then Satisfactory response 200
    """)
    context.execute_steps("""
        Given Integrating login module
        And Adding product_id in url for get product
        When Getting product
        Then Satisfactory response 200
        And Saving product in global
    """)
    time.sleep(2)
