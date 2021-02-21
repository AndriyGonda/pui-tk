from pui_tk.widgets import Button
from pui_tk import Application
from tkinter import PhotoImage
if __name__ == '__main__':
    app = Application()
    btn = Button(app, text='test')
    app.pack(btn)
    app.run()
