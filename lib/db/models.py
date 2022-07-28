from sqlalchemy import Column, Integer, column
from sqlalchemy.orm import Query
from lib.db.expecptions import ValidationError
from lib.screens.exception_detail import ExceptionScreen
from .session import session
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    id = Column('id',Integer,primary_key=True)
    session = session()

    def get_validation_methods(self):
        return [
            attribute
            for attribute in dir(self)
            if 'validate_' == attribute[0:9]
        ]

    class Meta:
        order_by_expression = lambda:BaseModel.id.asc()
    
    @property
    def get_session(self):
        try:
            return self.session
        except:
            self.session = session()
            return self.session

    def close_session(self):
        self.get_session.close()

    def validate(self):
        self.errors = {}
        for validation in self.get_validation_methods():
            column = validation.replace('validate_','')
            if hasattr(self,column):
                try:
                    getattr(self,validation)()
                except ValidationError as e:
                    if not column in self.errors.keys():
                        self.errors[column] = []
                    self.errors[column].append(str(e))
                except Exception as e:
                    if not '__all__' in self.errors.keys():
                        self.errors['__all__'] = []
                    self.errors['__all__'].append(str(e))
            else:
                raise AttributeError(column)
        if self.errors.keys():
            ExceptionScreen(ValidationError(self.errors),title='Erro de validação')

    def save(self):
        if not self.id:
            self.create()
        else:
            self.validate()
            self.get_session.commit()
            self.close_session()

    def delete(self):
        self.get_session.delete(self)
        self.get_session.commit()
        self.close_session()
    
    def create(self,**kwargs):
        obj = self.__class__()
        obj.__dict__.update(**kwargs)
        obj.validate()
        self.get_session.add(obj)
        self.get_session.commit()
        self.close_session()
        return obj

    def get_all(self):
        return self.query.all()

    @property
    def get_ordered(self):
        return self.query.order_by(self.Meta.order_by_expression)

    @property
    def query(self) -> Query:
        query = self.get_session.query(self.__class__)
        self.close_session()
        return query

