''' Function which creates a new independent session '''
from sqlalchemy.orm import sessionmaker
from app import db

def create_new_session():
    ''' Import db engine and create the session '''
    engine = db.get_engine()
    session = sessionmaker(bind=engine, expire_on_commit=False)
    new_session = session()
    return new_session
