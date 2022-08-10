from lib.db.models import BaseModel
from lib.db.expecptions import ValidationError
from sqlalchemy import Column,Integer,String
from lib.utils import get_hex_color, get_salutation
import pyperclip
from datetime import datetime


MAX_TITLE_LENGTH = 30
MAX_TEXT_LENGTH = 700
class FastAnswer(BaseModel):
    __tablename__ = 'fastanswer'
    title:str = Column('título',String(MAX_TITLE_LENGTH),nullable=False)
    priority_number:int = Column('prioridade',Integer,nullable=False)
    text:str = Column('texto',String(MAX_TEXT_LENGTH),nullable=False)
    text_color:str = Column('cor do texto',String,nullable=False)
    button_color:str = Column('cor do botão',String,nullable=False)

    class Meta:
        order_by_expression = lambda:FastAnswer.priority_number.asc()

    def get_updatable_fields(self):
        return (
            'title','priority_number','text','text_color','button_color','id'
        )

    def get_cleaned_text(self):
        return self.text.replace('[saudacao]',get_salutation())

    def copy_text(self):
        pyperclip.copy(self.get_cleaned_text())
        print('texto copiado')

    def set_text_color(self):
        self.text_color = get_hex_color()
    
    def set_button_color(self):
        self.button_color = get_hex_color()

    def validate_title(self):
        if not self.title:
            raise ValidationError('o título não pode estar vazio')
        if len(self.title) > MAX_TITLE_LENGTH:
            raise ValidationError(f'O título não pode ter mais que {MAX_TITLE_LENGTH} caracteres')
    
    def validate_text(self):
        if not self.text:
            raise ValidationError('o texto não pode estar vazio')
        if len(self.text)>MAX_TEXT_LENGTH:
            raise ValidationError(f'O texto não pode ter mais que {MAX_TEXT_LENGTH} caracteres')

    def validate_button_color(self):
        if not self.button_color:
            raise ValidationError('a cor do botão não pode ficar vazia')
        if not len(self.button_color) == 7:
            raise ValidationError('cor do botão inválida')

    def validate_text_color(self):
        if not self.text_color:
            raise ValidationError('a cor do texto não pode ficar vazia')
        if not len(self.text_color) == 7:
            raise ValidationError('cor do texto inválida')

    def validate_priority_number(self):
        if not str(self.priority_number):
            raise ValidationError('a prioridade não pode ficar vazia')




   

