from tkinter import IntVar
from pui_tk.widgets.radio_button import Radiobutton
from pui_tk import Application

if __name__ == '__main__':
    app = Application()
    var = IntVar()
    var.set(1)
    rb1 = Radiobutton(app, text='rb1', value=1, variable=var)
    rb2 = Radiobutton(app, text='rb2', value=2, variable=var)

    @app.event('a')
    def print_var(w, e):
        print(var.get())

    app.pack(rb1)
    app.pack(rb2)
    app.run()
