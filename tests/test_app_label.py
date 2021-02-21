from pui_tk import Application
from pui_tk.widgets import Label
from pui_tk.widgets import Entry
from tkinter import Event
from pui_tk.widgets.layouts import Row
from pui_tk.types import Cursor, Justify, EventType

if __name__ == '__main__':
    app = Application()
    app.set_min_size(400, 200)
    row = Row(app)
    row.tk_ref.pack(fill='both')
    label = Label(row, text='green', color='red', cursor=Cursor.DOT)
    # label.wrap_len = 200
    # #label.text = 'Test\nfdffddfdssssssss'
    # label.font = ['Sans Serif', 15, 'bold']
    # label.color = 'yellow'
    # label.bg_color = 'green'
    # label.justify = Justify.CENTER
    # label.underline = 0
    #label.cursor = Cursor.DOTBOX
    row.append(label, expand=True, fill=True)
    app.run()
