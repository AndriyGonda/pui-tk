from tkinter.ttk import Radiobutton as _TkRadiobutton
from .ui_widget import UiWidget


class Radiobutton(UiWidget):
    widget_class = _TkRadiobutton
