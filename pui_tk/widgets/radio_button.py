from tkinter.ttk import Radiobutton as _TkRadiobutton
from . import UiWidget


class Radiobutton(UiWidget):
    widget_class = _TkRadiobutton
