from tkinter import *

from lib.models.fast_answer import FastAnswer
from lib.utils import get_screen_height, get_screen_width


screen = Tk()
screen.title('Respostas Rápidas')
height = get_screen_height(screen)
width = get_screen_width(screen)
SCREEN_WIDTH = int(width*0.15)
SCREEN_HEIGHT = int(height*0.60)
screen.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}+{int(width*0.85/2)}+{int(height*0.4/2)}')
screen.iconbitmap('./assets/icon.ico')
screen.resizable(width=False,height=False)

fastAnswer:FastAnswer
for fastAnswer in FastAnswer().query.all():
    button = Button(
        screen,text=fastAnswer.title,command=lambda:fastAnswer.copy(screen),
        bg=fastAnswer.button_color,fg=fastAnswer.text_color,font="Consolas 11 bold",
        width=int(SCREEN_WIDTH*0.75)
    )
    button.pack(padx=SCREEN_WIDTH*0.07,pady=SCREEN_HEIGHT*0.01)
    button.bind('<Button-2>',fastAnswer.open_edit_screen)