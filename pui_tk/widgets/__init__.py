from typing import Callable
from pui_tk import Application
from tkinter import Event, Widget
from pui_tk.types import EventType


class _WidgetMeta(type):
    def __new__(mcs, name, bases, attrs):
        widget_class = attrs.get('widget_class')
        klass = super().__new__(mcs, name, bases, attrs)
        setattr(klass, 'widget_class', widget_class)
        return klass


class UiWidget(object, metaclass=_WidgetMeta):
    widget_class = Widget

    def __init__(self, base_widget, *args, **kwargs):
        if isinstance(base_widget, Application) or isinstance(base_widget, UiWidget):
            self.tk_ref = self.widget_class(base_widget.tk_ref, *args, **kwargs)
        else:
            raise TypeError(f'{type(base_widget)} is not Application or UiWidget')
        self.parent = base_widget

    def bind_event(self, event_type: EventType or str, callback: Callable[[Widget, Event], None]):
        """
        Bind event to application window
        :param event_type: EventType or str
        :param callback: function (widget, event)
        """
        self.tk_ref.bind(event_type, lambda event: callback(self, event))

    def event(self, event_type):
        """
        Decorator for bind_event function
        :param event_type: EventType or str
        """
        def _decorator(callback):
            self.bind_event(event_type, callback)
        return _decorator


