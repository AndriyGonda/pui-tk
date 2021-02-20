from pui_tk.widgets import UiWidget
from pui_tk.widgets import Frame


class Grid(Frame):
    def __init__(self, base_widget, **kwargs):
        super().__init__(base_widget, **kwargs)
    def add(
            self,
            row: int,
            col: int,
            widget: UiWidget,
            margin_x: int or tuple = (0, 0),
            margin_y: int or tuple = (0, 0),
            padding_x=0,
            padding_y=0
    ):
        widget.tk_ref.grid(
            row=row,
            column=col,
            ipadx=padding_x,
            ipady=padding_y,
            padx=margin_x,
            pady=margin_y
        )
