from tkinter.ttk import Label as _Label
from . import UiWidget


class Label(UiWidget):
    widget_class = _Label

    @property
    def text(self) -> str:
        return self.tk_ref['text']

