''' Módulo para las operaciones en base de datos '''
import click
from flask_babel import gettext
from models.product_company import ProductCompany
from models.product_country import ProductCountry
from models.stock_movement import StockMovement

def add_stock_movement(stock_movement, flask_app, db):
    """ Comandos para movimientos de stock """

    @stock_movement.cli.command('update_stock_from_requisition')
    @click.argument('data', nargs=7)
    # pylint: disable=unused-variable
    def update_stock_from_requisition(data):
        """Update stock from requisition"""
        type_action = data[0]
        code = data[1]
        user_id = data[2]
        company_id = data[3]
        product_id = data[4]
        field = data[5]
        amount = data[6]
        product_company = ProductCompany.query \
        .join(ProductCountry, ProductCountry.id == ProductCompany.product_country_id) \
        .filter(
            ProductCompany.company_id == company_id,
            ProductCountry.product_id == product_id,
            ProductCompany.deleted == "false"
        ).first()
        if product_company:
            old_stock = int(getattr(product_company, field))
            new_stock = old_stock + int(amount)
            setattr(product_company, field, new_stock)
            db.session.commit()

            description = ""
            if type_action == "1":
                description = gettext('New requisition with code {}')
            if type_action == "2":
                description = gettext('Requisition approved with code {}')
            if type_action == "3":
                description = gettext('Requisition with code {} was no longer approved')
            if type_action == "4":
                description = gettext('Requisition Product modified with code {}')
            if type_action == "5":
                description = gettext('Requisition Product deleted with code {}')
            if type_action == "6":
                description = gettext('New requisition product with code {}')
            description = description.format(code)

            stock_movement = StockMovement(
                user_id=user_id,
                product_company_id=product_company.id,
                field=field,
                amount=amount,
                old_stock=old_stock,
                new_stock=new_stock,
                description=description
            )
            db.session.add(stock_movement)
            db.session.commit()

            flask_app.logger.info("Stock successfully updated")
        else:
            flask_app.logger.info("Entity ProductCompany not found")

    flask_app.register_blueprint(stock_movement)
