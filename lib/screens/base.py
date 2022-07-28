from tkinter import Tk

from lib.utils import get_screen_height, get_screen_width


class BaseScreen(Tk):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.iconbitmap('./assets/icon.ico')
        self.MONITOR_HEIGHT= get_screen_height(self)
        self.MONITOR_WIDTH = get_screen_width(self)
        self.SCREEN_WIDTH = int(self.MONITOR_WIDTH*0.15)
        self.SCREEN_HEIGHT = int(self.MONITOR_HEIGHT*0.60)