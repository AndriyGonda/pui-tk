from typing import Callable
from tkinter import Event, Widget
from pui_tk.types import EventType
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)


class Chart(object):

    def __init__(self, base_widget):
        self.figure = Figure()
        self.canvas = FigureCanvasTkAgg(figure=self.figure, master=base_widget.tk_ref)
        self.canvas.draw()

    def clear(self):
        self.figure.clear()

    def refresh(self):
        self.canvas.draw()
        self.canvas.flush_events()

    def bind_event(self, event_type: EventType or str, callback: Callable[[Widget, Event], None]):
        """
        Bind event to application window
        :param event_type: EventType or str
        :param callback: function (widget, event)
        """
        self.canvas.get_tk_widget().bind(event_type, lambda event: callback(self, event))

    def event(self, event_type):
        """
        Decorator for bind_event function
        :param event_type: EventType or str
        """

        def _decorator(callback):
            self.bind_event(event_type, callback)

        return _decorator