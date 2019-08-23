# For getting environment variables
import os

# For ORM database engine management
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')

# Configure engine (dialect and driver)
engine = create_engine('mysql+pymysql://' + DB_USER + ':' + DB_PASS + '@' + DB_HOST + ':' + DB_PORT + '/' + DB_NAME, echo=True)
Session = sessionmaker(bind=engine)