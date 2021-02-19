from pui_tk import Application
from pui_tk.types import EventType

app = Application()


@app.event(event_type=EventType.LEFT_BUTTON_CLICK)
def click(target: Application, event):
    print('left click')
    print(event)


@app.event(event_type=EventType.RIGHT_BUTTON_CLICK)
def right_click(target: Application, event):
    print(target.height)
    print(event)


@app.event(event_type=EventType.MIDDLE_BUTTON_CLICK)
def middle_click(target: Application, event):
    print(target.width)
    print(event)


if __name__ == '__main__':
    app.height = 400
    app.width = 400
    app.always_top = True
    app.run()
