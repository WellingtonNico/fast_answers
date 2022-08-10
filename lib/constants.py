from PyQt6.QtCore import Qt
from pathlib import Path


DEFAULT_FONT = "Consolas 11 bold"
ONTOP_FLAG = Qt.WindowType.WindowStaysOnTopHint
ONBOTTOM_FLAG = Qt.WindowType.WindowStaysOnBottomHint
BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = f'{BASE_DIR}/assets/'