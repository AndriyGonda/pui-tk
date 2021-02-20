from tkinter.ttk import Checkbutton as _Checkbox
from tkinter import BooleanVar
from .ui_widget import UiWidget


class Checkbox(UiWidget):
    widget_class = _Checkbox

    def __init__(self, *args, **kwargs):
        self._state = BooleanVar()
        self._state.set(0)
        super().__init__(*args, **kwargs, variable=self._state, onvalue=1, offvalue=0)

    @property
    def checked(self) -> bool:
        return self._state.get()

    @checked.setter
    def checked(self, value: bool):
        self._state.set(value)
