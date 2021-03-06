from pui_tk.widgets import UiWidget
from pui_tk.widgets import Frame


class Column(Frame):
    def __init__(self, base_widget, **kwargs):
        super().__init__(base_widget, **kwargs)

    @staticmethod
    def append(widget: UiWidget, expand=False, fill=False):
        widget.tk_ref.pack(side='top', fill='both' if fill else 'none', expand=expand)

    @staticmethod
    def append_reverse(widget: UiWidget, expand=False, fill=False):
        widget.tk_ref.pack(side='bottom', fill='both' if fill else 'none', expand=expand)
