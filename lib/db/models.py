from sqlalchemy import Column, Integer, column
from sqlalchemy.orm import Query

from lib.db.expecptions import ValidationError
from .session import session
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    id = Column('id',Integer,primary_key=True)
    session = session

    def get_validation_methods(self):
        return [
            attribute
            for attribute in dir(self)
            if 'validate_' == attribute[0:9]
        ]

    class Meta:
        order_by_expression = lambda:BaseModel.id.asc()

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
            raise ValidationError(self.errors)

    def save(self):
        self.validate()
        self.session.commit()

    def delete(self):
        self.session.delete(self)
        self.session.commit()
    
    def create(self,**kwargs):
        obj = self.__class__()
        obj.__dict__.update(**kwargs)
        obj.validate()
        self.session.add(obj)
        self.session.commit()
        return obj

    def get_all(self):
        return self.query.all()

    @property
    def query(self) -> Query:
        return self.session.query(self.__class__).order_by(self.Meta.order_by_expression)
