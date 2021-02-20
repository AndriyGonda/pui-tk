from pui_tk import Application
from pui_tk.widgets import Frame, Button, Radiobutton, Entry, LabeledEntry, Checkbox

if __name__ == '__main__':
    app = Application()
    app.set_min_size(640, 480)
    form1 = Frame(app)
    form1.tk_ref.grid(row=0, column=0, sticky='nesw')
    edit1 = Entry(form1, text='edit1')
    btn1 = Button(form1, text='btn1')
    rb1 = Radiobutton(form1, text='rb1')
    cb1 = Checkbox(form1, text='cb1')
    lbl_edit = LabeledEntry(form1)
    lbl_edit.label.text = 'lbl_edit'
    lbl_edit.entry.text = 'lbl_edit text'
    btn1.tk_ref.grid(row=0, column=0)
    edit1.tk_ref.grid(row=1, column=1)
    rb1.tk_ref.grid(row=1, column=0)
    cb1.tk_ref.grid(row=0, column=1)
    lbl_edit.tk_ref.grid(row=2, column=1)
    app.run()
