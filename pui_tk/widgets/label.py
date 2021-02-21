from tkinter import Label as _Label
from tkinter import StringVar
from .ui_widget import UiWidget
from pui_tk.types import TkProperty, Cursor, Relief, Justify


class Label(UiWidget):
    widget_class = _Label
    text = TkProperty('text', str)  # Label text
    width = TkProperty('width', int)  # Label width
    font = TkProperty('font', (tuple, list))  # Label Font
    wrap_len = TkProperty('wraplength', int)  # Label wrap length in pixels
    color = TkProperty('fg', str)  # text color
    bg_color = TkProperty('bg', str)  # background color
    underline = TkProperty('underline', int)  # underline character in n position
    justify: str = TkProperty('justify', (Justify, str))  # justify multiline text left, center, right
    bitmap = TkProperty('bitmap')  # label bitmap object
    image = TkProperty('image')  # label image object
    relief = TkProperty('relief', (Relief, str))  # label relief
    cursor = TkProperty('cursor', (Cursor, str))  # label cursor
    border_size = TkProperty('bd', int)  # border size in pixels
    padx = TkProperty('padx', int)  # extra spaces added to the left and right
    pady = TkProperty('pady', int)  # extra spaces added to the top and bottom

    def __init__(self, base_widget, **kwargs):
        super().__init__(base_widget, **kwargs)
        self._text_var = StringVar()

    @property
    def textvar(self) -> str:
        return self._text_var.get()

    @textvar.setter
    def textvar(self, value: str):
        self._text_var.set(value)



