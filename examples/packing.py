from pui_tk import Application
from pui_tk.types import Side
from pui_tk.widgets import Label


if __name__ == '__main__':
    app = Application('Packing examples')
    app.pack(Label(app, text='pack-left'), side=Side.LEFT)
    app.pack(Label(app, text='pack-right'), side=Side.RIGHT)
    app.pack(Label(app, text='pack-top'), side=Side.TOP)
    app.pack(Label(app, text='pack-bottom'), side=Side.BOTTOM)
    app.place(Label(app, text='place'), x=200, y=250)

    app.run()
