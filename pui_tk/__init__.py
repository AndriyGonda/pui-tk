from tkinter import Tk, Widget, Event
from .types import EventType
from typing import Callable


class Application(object):
    """
     Application class for Tkinter root instance
     The tkinter reference (tk_ref) can be use if needed for setting custom properties
    """

    def __init__(self, title='Application'):
        self.tk_ref: Tk = Tk()
        self.title = title

    @property
    def title(self) -> str:
        """
        @property title for root window
        :return: title of root window
        """
        return self.tk_ref.title()

    @title.setter
    def title(self, value: str):
        """
        Set root window title
        :param value: str - title of root window
        """
        self.tk_ref.title(value)

    @property
    def height(self) -> int:
        """
        get root window height
        :return: int - window height
        """
        self.tk_ref.update()
        return self.tk_ref.winfo_height()

    @height.setter
    def height(self, value: int):
        """
        set root window height
        :param value: int - window height
        """
        self.tk_ref.geometry(f'{self.width}x{value}')

    @property
    def width(self) -> int:
        """
        get root window width
        :return: int - window width
        """
        self.tk_ref.update()
        return self.tk_ref.winfo_width()

    @width.setter
    def width(self, value: int):
        """
        set root window width
        :param value: int - window width
        """
        self.tk_ref.geometry(f'{value}x{self.height}')

    @property
    def offset_x(self) -> int:
        """
        Get root window offset x in pixels value
        :return: int - x offset
        """
        self.tk_ref.update()
        return self.tk_ref.winfo_x()

    @offset_x.setter
    def offset_x(self, x: int):
        """
        Set root window x offset in pixels
        :param x: int
        """
        self.tk_ref.geometry(f'{self.width}x{self.height}+{x}+{self.offset_y}')

    @property
    def offset_y(self) -> int:
        """
        Get root window offset y in pixels value
        :return: int - y offset
        """
        self.tk_ref.update()
        return self.tk_ref.winfo_y()

    @offset_y.setter
    def offset_y(self, y: int):
        """
        Set root window y offset in pixels
        :param y: int
        """
        self.tk_ref.geometry(f'{self.width}x{self.height}+{self.offset_x}+{y}')

    def set_min_size(self, width: int, height: int):
        """
        Set minimal window size in pixels
        :param width: int - window width
        :param height: int - window height
        """
        self.tk_ref.minsize(width=width, height=height)

    def set_max_size(self, width: int, height: int):
        """
        Set maximal window size in pixels
        :param width: int - window  width
        :param height: int - window height
        """
        self.tk_ref.maxsize(width=width, height=height)

    def set_fixed_size(self):
        self.tk_ref.resizable(False, False)

    @property
    def background(self) -> str:
        """
        Get background window color code
        :return: str (hex color code #ee1112 for example)
        """
        return self.tk_ref.config()['background'][-1]

    @background.setter
    def background(self, color: str):
        """
        Set background window color
        :param color: str - hex code of color or standalone constant from Tkinter
        """
        self.tk_ref.configure(background=color)

    @property
    def alpha(self) -> float:
        """
        Get window opacity value
        :return: float (in range 0..1)
        """
        return float(self.tk_ref.wm_attributes('-alpha'))

    @alpha.setter
    def alpha(self, value: float):
        """
        Set window opacity value
        :param value: float (in range 0..1)
        """
        self.tk_ref.wm_attributes('-alpha', value)

    @property
    def fullscreen(self) -> bool:
        """
        Check if fullscreen mode enabled
        :return: True or False
        """
        return bool(self.tk_ref.wm_attributes('-fullscreen'))

    @fullscreen.setter
    def fullscreen(self, value: bool):
        """
        Enable fullscreen mode
        :param value: True or False
        """
        self.tk_ref.wm_attributes('-fullscreen', int(value))

    @property
    def always_top(self) -> bool:
        """
        Check if always top window mode enabled
        :return: True or False
        """
        return bool(self.tk_ref.wm_attributes('-topmost'))

    @always_top.setter
    def always_top(self, value: bool):
        """
        Enable/Disable always top window mode
        :param value: True or False
        """
        self.tk_ref.wm_attributes('-topmost', int(value))

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

    def run(self):
        """
        Run application mainloop
        """
        self.tk_ref.mainloop()
