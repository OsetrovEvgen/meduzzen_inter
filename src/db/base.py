from databases import Database
from sqlalchemy import create_engine, MetaData
from starlette.config import Config
from config import settings
from sqlalchemy.orm import sessionmaker

config = Config('.env')
DATABASE_URL = config('MED_DATABASE_URL', cast=str, default='')
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = 'HS256'
SECRET_KEY = settings.MED_SECRET_KEY
databases = Database(DATABASE_URL)
engine = create_engine(
    DATABASE_URL,
)
Session = sessionmaker(bind=engine)
session = Session()
