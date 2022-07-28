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
        self.mainFrame = Frame(self)
        self.mainFrame.pack(fill=BOTH,expand=1)

        self.mainCanvas = Canvas(self.mainFrame)
        self.mainCanvas.pack(side=LEFT,fill=BOTH,expand=1)

        self.mainScrollBar = Scrollbar(self.mainFrame,orient=VERTICAL,command=self.mainCanvas.yview)
        self.mainScrollBar.pack(side=LEFT,fill=Y)
        self.mainCanvas.configure(yscrollcommand=self.mainScrollBar.set)
        self.mainCanvas.bind('<Configure>',lambda e:self.mainCanvas.configure(scrollregion=self.mainCanvas.bbox('all')))
        self.mainSecondFrame = Frame(self.mainCanvas)
        self.mainCanvas.create_window((0,0),window=self.mainSecondFrame,anchor='nw')

        self.build_update_button()
        self.build_add_button()
        self.build_list()

    def build_list(self):
        fastAnswer:FastAnswer
        for fastAnswer in FastAnswer().get_ordered.all():
            fastAnswer.append_button(self,self.mainSecondFrame)
    
    def build_add_button(self):
        button = Button(
            self.mainSecondFrame,text='+ adicionar',
            bg='blue',fg='white',font="Consolas 11 bold",
            command=lambda:FastAnswerFormScreen(fastAnswerClass=FastAnswer).mainloop(),
            anchor=S
        )
        button.pack()

    def build_update_button(self):
        button = Button(
            self.mainSecondFrame,text='atualizar',
            bg='blue',fg='white',font="Consolas 11 bold",
            command=lambda:FastAnswerFormScreen(fastAnswerClass=FastAnswer).mainloop(),
            anchor=N
        )
        button.pack()
 
    def destroy(self) -> None:
        return super().withdraw()