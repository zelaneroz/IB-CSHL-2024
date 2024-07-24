from sqlalchemy import Integer, Column,String,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class user (Base):
    id = Column(Integer, primary_key=True)
    username = Column(String(250),unique=True)
    email=Column(String(250), unique=True, nullable=False)
    password = Column(String(300))

engine = create_engine('sqlite:///orm_login_db.db')
Base.metadata.create_all(engine)

#Configuration
Base.metadata.bind = engine
session = sessionmaker(bind=engine)
my_session = session()

result = my_session.query(user).all()
for r in result:
    print(r.username)
#create_user

