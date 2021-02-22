from tkinter.ttk import Radiobutton as _TkRadiobutton
from .ui_widget import UiWidget
from pui_tk.types import TkProperty, Cursor, Side


class Radiobutton(UiWidget):
    widget_class = _TkRadiobutton
    variable = TkProperty('variable')
    value = TkProperty('value')
    textvariable = TkProperty('textvariable')
    text = TkProperty('text', str)
    style = TkProperty('style', str)
    cursor = TkProperty('cursor', (Cursor, str))
    image = TkProperty('image', str)
    underline = TkProperty('underline', int)
    compound = TkProperty('compound', (Side, str))
    width = TkProperty('width', int)
