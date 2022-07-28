from datetime import datetime
from tkinter import colorchooser


def get_hex_color():
    return colorchooser.askcolor()[1]

def get_screen_width(screen):
    return screen.winfo_screenwidth()

def get_screen_height(screen):
    return screen.winfo_screenheight()

def get_salutation() -> str:
    if datetime.now().hour >= 4 and datetime.now().hour <= 11:
        return f'bom dia'
    if datetime.now().hour >= 12 and datetime.now().hour <= 17:
        return f'boa tarde'
    if datetime.now().hour >= 18 and datetime.now().hour <= 23:
        return f'boa noite'
    if datetime.now().hour >= 0 and datetime.now().hour <= 3:
        return f'boa noite'