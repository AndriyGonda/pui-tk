from tkinter.ttk import Checkbutton as _Checkbox
from tkinter import BooleanVar
from .ui_widget import UiWidget
from pui_tk.types import TkProperty, Cursor, Side


class Checkbox(UiWidget):
    widget_class = _Checkbox
    onvalue = TkProperty('onvalue', int)
    offvalue = TkProperty('offvalue', int)
    variable = TkProperty('variable', BooleanVar)
    text = TkProperty('text', str)
    style = TkProperty('style', str)
    cursor = TkProperty('cursor', (Cursor, str))
    image = TkProperty('image', str)
    underline = TkProperty('underline', int)
    compound = TkProperty('compound', (Side, str))
    width = TkProperty('width', int)

    def __init__(self, parent, *args, **kwargs):
        self._state = BooleanVar()
        self._state.set(0)
        super().__init__(parent, *args, **kwargs, variable=self._state, onvalue=1, offvalue=0)

    @property
    def checked(self) -> bool:
        return self._state.get()

    @checked.setter
    def checked(self, value: bool):
        self._state.set(value)
