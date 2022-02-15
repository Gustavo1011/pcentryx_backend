"""
code.py: Librería para generar codigos
"""
from sqlalchemy import func
from app import db

def generate_code(cls, predigits):
    ''' Method to generate codes '''
    count_codes = db.session.query(func.count('*')).select_from(cls).scalar()
    pre_zeros = "0" * (predigits - len(str(count_codes + 1)))
    next_code = pre_zeros + str(int(count_codes) + 1)
    return next_code

def generate_code_by_number(code_number, predigits):
    ''' Method to generate code by nummber '''
    pre_zeros = "0" * (predigits - len(str(code_number + 1)))
    next_code = pre_zeros + str(int(code_number) + 1)
    return next_code
