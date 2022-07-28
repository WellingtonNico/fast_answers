from tkinter import *

from lib.models.fast_answer import FastAnswer
from lib.utils import get_screen_height, get_screen_width


screen = Tk()
screen.title('Respostas Rápidas')
height = get_screen_height(screen)
width = get_screen_width(screen)
screen.geometry(f'{int(width*0.15)}x{int(height*0.60)}+{int(width*0.85/2)}+{int(height*0.4/2)}')
screen.iconbitmap('./assets/icon.ico')
screen.resizable(width=False,height=False)

fastAnswer:FastAnswer
for fastAnswer in FastAnswer().query.all():
    Button(
        screen,text=fastAnswer.title,command=lambda:fastAnswer.copy(screen),
        bg=fastAnswer.button_color,fg=fastAnswer.text_color,font="Consolas 11 bold",
    ).pack()