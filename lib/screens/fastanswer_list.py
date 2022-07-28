from tkinter import *
from lib.models.fast_answer import FastAnswer
from lib.screens.base import BaseScreen
from lib.screens.fastanswer_form import FastAnswerFormScreen


class FastAnswerListScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Respostas Rápidas')
        self.geometry(f'{self.SCREEN_WIDTH}x{self.SCREEN_HEIGHT}+{int(self.MONITOR_WIDTH*0.85/2)}+{int(self.MONITOR_HEIGHT*0.4/2)}')
        self.resizable(width=False,height=False)
        self.build_list()
        self.build_add_button()

    def build_list(self):
        fastAnswer:FastAnswer
        for fastAnswer in FastAnswer().get_ordered.all():
            fastAnswer.append_button(self)
    
    def build_add_button(self):
        button = Button(
            self,text='+ adicionar',
            bg='blue',fg='white',font="Consolas 11 bold",
            command=lambda:FastAnswerFormScreen(fastAnswerClass=FastAnswer).mainloop(),
            anchor=S
        )
        button.pack()
 