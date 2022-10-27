import sqlalchemy
import datetime

from sqlalchemy import Column
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True)
    email = Column('email', sqlalchemy.String, primary_key=True, unique=True)
    name = Column('name', sqlalchemy.String)
    hashed_password = Column('hashed_password', sqlalchemy.String)
    is_company = Column('is_company', sqlalchemy.Boolean)
    created_at = Column('created_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow)
    updated_at = Column('updated_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name,
            self.fullname,
            self.nickname,
        )
