from databases import Database
from sqlalchemy import create_engine, MetaData
from starlette.config import Config
from config import settings


config = Config('.env')
DATABASE_URL = config('MED_DATABASE_URL', cast=str, default='')
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = 'HS256'
SECRET_KEY = config('MED_SECRET_KEY', cast=str, default=settings.SECRET_KEY)
databases = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(
    DATABASE_URL,
)
