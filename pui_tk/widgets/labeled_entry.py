from tkinter.ttk import Frame as _Frame
from .frame import Frame
from .label import Label
from .entry import Entry
from . import UiWidget

class LabeledEntry(Frame):
    widget_class = _Frame

    def __init__(self, base_widget):
        super().__init__(base_widget)
        self.label = Label(self, text='Label12', justify='left')
        self.entry = Entry(self, text='entry1')
        self.label.tk_ref.grid(row=0, column=0)
        self.entry.tk_ref.grid(row=1, column=0)
        self.label.grid = self.label.tk_ref.grid
        self.entry.grid = self.entry.tk_ref.grid
