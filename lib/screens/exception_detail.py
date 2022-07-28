from tkinter import Button, Label

from lib.constants import DEFAULT_FONT
from .base import BaseScreen


class ExceptionScreen(BaseScreen):
    def __init__(self,exc:Exception, title='Erro!',*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Erro')
        Label(self,text=title,font=DEFAULT_FONT,pady=int(self.SCREEN_HEIGHT*0.05)).pack()
        Label(self,text=str(exc),font=DEFAULT_FONT,fg='red',pady=int(self.SCREEN_HEIGHT*0.08)).pack()
        Button(self,text='ok',command=self.destroy).pack()

