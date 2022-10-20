from databases import Database
from sqlalchemy import create_engine, MetaData
from starlette.config import Config


config = Config('.env')
DATABASE_URL = config('MED_DATABASE_URL', cast=str, default='')
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = 'HS256'
SECRET_KEY = config('MED_SECRET_KEY', cast=str, default='eba7eb9bd5913aaaaf6164c71558b196ef70ddb4afe065b4a66885b16b9c0b0f')
databases = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(
    DATABASE_URL,
)

