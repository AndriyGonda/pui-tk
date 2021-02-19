from pui_tk import Application
from pui_tk.types import EventType
from pui_tk.widgets.button import Button
from pui_tk.widgets.radio_button import Radiobutton
from pui_tk.widgets.checkbox import Checkbox
from pui_tk.widgets.entry import Entry
from pui_tk.widgets.label import Label
from pui_tk.widgets.labeled_entry import LabeledEntry
app = Application()


if __name__ == '__main__':
    app.height = 400
    app.width = 400
    lbl_entry = LabeledEntry(app)

    lbl_entry.tk_ref.pack()
    app.always_top = True
    app.run()
