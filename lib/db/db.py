from .models import Base
from .session import Engine

def create_database():
    Base.metadata.create_all(bind=Engine)
