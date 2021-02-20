from pui_tk.widgets import UiWidget
from pui_tk.widgets import Frame


class Row(Frame):
    def __init__(self, base_widget, **kwargs):
        super().__init__(base_widget, **kwargs)

    @staticmethod
    def append(widget: UiWidget, expand=False, fill=False):
        widget.tk_ref.pack(side='left', fill='both' if fill else 'none', expand=expand)

    @staticmethod
    def append_reverse(widget: UiWidget, expand=False, fill=False):
        widget.tk_ref.pack(side='right', fill='both' if fill else 'none', expand=expand)
