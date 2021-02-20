from pui_tk import Application
from pui_tk.types import EventType
from pui_tk.widgets.button import Button
from pui_tk.widgets.radio_button import Radiobutton
from pui_tk.widgets.checkbox import Checkbox
from pui_tk.widgets.entry import Entry
from pui_tk.widgets.label import Label
from pui_tk.widgets.labeled_entry import LabeledEntry
from pui_tk.widgets.chart import Chart
app = Application()
from math import sin


if __name__ == '__main__':
    app.height = 400
    app.width = 400
    btn = Button(app, text='start')
    chart = Chart(app)
    chart.canvas.get_tk_widget().pack(fill='both')
    gr1 = chart.figure.subplots()
    chart.refresh()

    @btn.event(event_type=EventType.LEFT_BUTTON_CLICK)
    def plot_y(widget: Button, event):
        x_array = []
        y_array = []
        gr1.clear()
        dx = 0.1
        for i in range(100):
            x_array.append(i*dx)
            y_array.append(sin(i*dx))
            gr1.plot(x_array, y_array, 'g-')
            chart.refresh()

    @chart.event(event_type=EventType.LEFT_BUTTON_CLICK)
    def chart_click(widget: Chart, event):
        print(widget)
        print(event)

    btn.tk_ref.pack(side='left')
    app.always_top = True
    app.run()
