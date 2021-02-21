from typing import Callable
from pui_tk import Application
from tkinter import Event, Widget
from pui_tk.types import EventType, State, TkProperty


class UiWidget(object):
    widget_class = Widget
    state = TkProperty('state', (State, str))

    def __init__(self, base_widget, *args, **kwargs):
        if isinstance(base_widget, Application) or isinstance(base_widget, UiWidget):
            self.tk_ref = self.widget_class(base_widget.tk_ref, *args)
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            raise TypeError(f'{type(base_widget)} is not Application or UiWidget')
        self.configure = self.tk_ref.configure
        self.parent = base_widget

    def bind_event(self, event_type: EventType or str, callback: Callable[[Widget, Event], None]):
        """
        Bind event to  widget
        :param event_type: EventType or str
        :param callback: function (widget, event)
        """
        self.tk_ref.bind(event_type, lambda event: callback(self, event))
        return callback

    def event(self, event_type):
        """
        Decorator for bind_event function
        :param event_type: EventType or str
        """
        def _decorator(callback):
            return self.bind_event(event_type, callback)
        return _decorator
