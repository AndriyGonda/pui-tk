from pui_tk import Application
from pui_tk.widgets import Frame, Button, Radiobutton, Entry, LabeledEntry, Checkbox
from pui_tk.widgets.layouts import Column, Row

if __name__ == '__main__':
    app = Application()
    app.set_min_size(640, 480)
    row = Row(app)
    btn1 = Button(row, text='1')
    btn2 = Button(row, text='2')
    row.append(btn1)
    row.append(btn2)

    col = Column(row)
    btn3 = Button(col, text='3')
    btn4 = Button(col, text='4')
    col.append(btn3)
    col.append(btn4)

    row.append(col)
    row.tk_ref.pack(side='left', expand=True, fill='both')
    app.run()
