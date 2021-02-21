from pui_tk import Application
from pui_tk.widgets import Checkbox

if __name__ == '__main__':
    app = Application()
    app.background = 'red'
    cb1 = Checkbox(app, text='test', checked=True)
    app.pack(cb1)
    app.run()
