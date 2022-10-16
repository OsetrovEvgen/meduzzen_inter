from databases import Database
from sqlalchemy import create_engine, MetaData
from starlette.config import Config


config = Config('.env')
DATABASE_URL = config('MED_DATABASE_URL', cast=str, default='')
databases = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(
    DATABASE_URL,
)

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
#
# SQLALCHEMY_DATABASE_URL = "postgresql://username:password@db:5432/nudges"
#
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine)
# Base = declarative_base()
#
