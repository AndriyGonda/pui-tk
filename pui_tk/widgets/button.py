from tkinter.ttk import Button as _Button
from .ui_widget import UiWidget


class Button(UiWidget):
    widget_class = _Button

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def text(self):
        return self.tk_ref['text']

    @text.setter
    def text(self, title: str):
        self.tk_ref['text'] = title
