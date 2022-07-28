from copy import copy
from tkinter import Tk
from lib.db.models import BaseModel
from lib.db.expecptions import ValidationError
from sqlalchemy import Column,Integer,String
from lib.utils import get_salutation
import pyperclip


class FastAnswer(BaseModel):
    __tablename__ = 'fastanswer'
    title:str = Column('título',String(30),nullable=False)
    priority_number:int = Column('prioridade',Integer,nullable=False)
    text:str = Column('texto',String(500),nullable=False)
    text_color:str = Column('cor do texto',String,nullable=False)
    button_color:str = Column('cor do botão',String,nullable=False)

    class Meta:
        order_by = ['id','priority_number']

    def paste(self,screen:Tk):
        textToCopy = self.text.replace('[saudacao]',get_salutation())
        pyperclip.copy(textToCopy)
        # screen.iconify()
        screen.withdraw()
        pyperclip.paste()


    def validate_title(self):
        if not self.title:
            raise ValidationError('O título não pode estar vazio')
    
    def validate_text(self):
        if not self.text:
            raise ValidationError('O texto não pode estar vazio')

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
        if not self.priority_number:
            raise ValidationError('a prioridade não pode ficar vazia')




   

