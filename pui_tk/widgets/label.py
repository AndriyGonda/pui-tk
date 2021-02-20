from tkinter.ttk import Label as _Label
from .ui_widget import UiWidget


class Label(UiWidget):
    widget_class = _Label

    @property
    def text(self) -> str:
        return self.tk_ref['text']

    @text.setter
    def text(self, value: str):
        self.tk_ref['text'] = value


