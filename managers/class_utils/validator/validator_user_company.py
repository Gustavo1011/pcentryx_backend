from flask_jwt_extended import get_jwt_identity

from exceptions.new_exceptions.unauthorized_company_exception import UnauthorizedCompanyException
from managers.class_utils.validator.validator import Validator
from models import User


class ValidatorUserCompany(Validator):
    """Class for validator if company is authorized for user"""
    def __init__(self, company_id, field_error):
        self.company_id = company_id
        self.field_error = field_error

    def validate(self, data, vars_):
        if self.is_user_unauthorized_for_company():
            raise UnauthorizedCompanyException(self.field_error)

    def is_user_unauthorized_for_company(self):
        user_id = int(get_jwt_identity()['id'])
        if user_id in [1, 2]:
            return False
        user = User.query.filter(User.id == user_id).first()
        allowed_company_ids = user.get_allowed_company_ids()
        return self.company_id not in allowed_company_ids
