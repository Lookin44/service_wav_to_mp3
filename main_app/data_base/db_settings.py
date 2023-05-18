import os

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker


db_config = {
    'drivername': 'postgresql+psycopg2',
    'host': 'db',
    'port': '5432',
    'username': os.environ.get('PSQL_USER'),
    'password': os.environ.get('PSQL_PASSWORD'),
    'database': os.environ.get('PSQL_DATABASE'),
}

database_url = URL.create(**db_config)
engine = create_engine(database_url)

Session = sessionmaker(bind=engine)
session = Session()
