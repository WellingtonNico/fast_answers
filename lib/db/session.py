from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Engine = create_engine('sqlite:///./database.db')
session = sessionmaker(bind=Engine)()