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

