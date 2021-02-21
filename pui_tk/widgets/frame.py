from tkinter.ttk import Frame as _Frame
from .ui_widget import UiWidget
from pui_tk.types import TkProperty, Cursor, Relief


class Frame(UiWidget):
    widget_class = _Frame
    style = TkProperty('style', str)
    takefocus = TkProperty('takefocus', bool)
    width = TkProperty('width', (int, str))
    height = TkProperty('height', (int, str))
    padding = TkProperty('padding', (int, str))
    cursor = TkProperty('cursor', (str, Cursor))
    relief = TkProperty('relief', (str, Relief))

