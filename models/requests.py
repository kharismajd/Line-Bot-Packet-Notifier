from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import JSON
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(String, primary_key=True)
    status = Column(String)
    argument = Column(String)

    def __repr__(self):
        return "<User(user_id='{}', status='{}', argument={})>"\
                .format(self.user_id, self.status, self.argument)

class Request(Base):
    __tablename__ = 'requests'
    user_id = Column(String)
    resi = Column(String, primary_key=True)
    kurir = Column(String, primary_key=True)
    status = Column(String)
    last_result = Column(JSON)
    last_update = Column(DateTime)

    def __repr__(self):
        return "<Request(user_id='{}', resi='{}', kurir={}, status={}, last_result={}, last_update={})>"\
                .format(self.user_id, self.resi, self.kurir, self.status, self.last_result, self.last_update)

class Request_Delivered(Base):
    __tablename__ = 'requests_delivered'
    user_id = Column(String)
    resi = Column(String, primary_key=True)
    kurir = Column(String, primary_key=True)
    status = Column(String)
    last_result = Column(JSON)
    last_update = Column(DateTime)

    def __repr__(self):
        return "<Request(user_id='{}', resi='{}', kurir={}, status={}, last_result={}, last_update={})>"\
                .format(self.user_id, self.resi, self.kurir, self.status, self.last_result, self.last_update)