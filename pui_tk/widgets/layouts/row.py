from pui_tk.widgets import UiWidget
from pui_tk.widgets import Frame


class Row(Frame):
    def __init__(self, base_widget):
        super().__init__(base_widget)
        self._columns = 0

    def append(self, widget: UiWidget,
               margin_x: int or tuple = (0, 5),
               margin_y: int or tuple = (0, 5),
               padding_x: int = 0,
               padding_y: int = 0,
               sticky='nsew'):
        widget.tk_ref.grid(
                row=0,
                column=self._columns,
                padx=margin_x,
                pady=margin_y,
                ipadx=padding_x,
                ipady=padding_y,
                sticky=sticky
            )
        self._columns += 1
