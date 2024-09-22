from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

def create_db_engine():
    db_url = URL.create(
        drivername='mysql+mysqlconnector',
        username=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        database=DB_NAME
    )
    engine = create_engine(db_url)
    return engine
