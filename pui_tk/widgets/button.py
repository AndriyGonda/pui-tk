from tkinter.ttk import Button as _Button
from .ui_widget import UiWidget
from pui_tk.types import TkProperty, Cursor, Side


class Button(UiWidget):
    widget_class = _Button
    text = TkProperty('text', str)
    style = TkProperty('style', str)
    cursor = TkProperty('cursor', (Cursor, str))
    image = TkProperty('image', str)
    underline = TkProperty('underline', int)
    compound = TkProperty('compound', (Side, str))
