from tkinter.ttk import Entry as _Entry
from tkinter import StringVar
from .ui_widget import UiWidget


class Entry(UiWidget):
    widget_class = _Entry

    def __init__(self, *args, **kwargs):
        self._string_var = StringVar()
        super().__init__(*args, **kwargs, textvariable=self._string_var)

    @property
    def text(self) -> str:
        return self._string_var.get()

    @text.setter
    def text(self, value: str):
        self._string_var.set(value)

