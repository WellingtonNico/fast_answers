from tkinter import *
from lib.constants import DEFAULT_FONT
from lib.db.expecptions import ValidationError

from lib.screens.base import BaseScreen
from lib.screens.exception_detail import ExceptionScreen


class FastAnswerFormScreen(BaseScreen):
    def __init__(self,fastAnswer=None,fastAnswerClass=None,*args,**kwargs) -> None:
        self.fastAsnwer = fastAnswer if fastAnswer else fastAnswerClass()
        super().__init__(*args,**kwargs)
        self.title('Formulário')
        Label(self,text='título:',font=DEFAULT_FONT).pack()
        Entry(self,textvariable=self.fastAsnwer.title).pack()
        Label(self,text='texto:',font=DEFAULT_FONT).pack()
        self.textEntry = Text(self,height=6)
        self.textEntry.pack()
        Label(self,text='Prioridade(quanto menor mais acima fica):',font=DEFAULT_FONT).pack()
        Label(self,text='cor do texto:',font=DEFAULT_FONT).pack()
        Button(self,text='     ',command=self.fastAsnwer.set_text_color,bg=self.fastAsnwer.text_color).pack()
        Label(self,text='cor do botão:',font=DEFAULT_FONT).pack()
        Button(self,text='     ',command=self.fastAsnwer.set_button_color,bg=self.fastAsnwer.button_color).pack()
        Button(self,text='salvar',font=DEFAULT_FONT,command=self.save,bg='green').pack()

    def save(self):
        self.fastAsnwer.text = self.textEntry.get(1.0,END)
        self.fastAsnwer.save()
        self.destroy()




