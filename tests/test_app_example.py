from pui_tk import Application
from pui_tk.widgets import Frame, Button, Radiobutton, Entry, LabeledEntry, Checkbox
from pui_tk.widgets.layouts import Column, Row, Grid

if __name__ == '__main__':
    app = Application()
    app.set_min_size(640, 480)
    row = Row(app)
    grid = Grid(row, bg='red')
    btn1 = Button(grid, text='1')
    btn2 = Button(grid, text='2')
    grid.add(0, 0, btn1, margin_y=20)
    grid.add(1, 0, btn2)
    row.append(grid)
    grid2 = Grid(row)
    btn3 = Button(grid2, text='3')
    btn4 = Button(grid2, text='4')
    grid.add(0, 0, btn3)
    grid.add(1, 0, btn4)
    row.append(grid2)
    # btn1 = Button(row, text='1')
    # btn2 = Button(row, text='2')
    # row.append(btn1)
    # row.append(btn2)
    #
    # col = Column(row)
    # btn3 = Button(col, text='3')
    # btn4 = Button(col, text='4')
    # col.append(btn3)
    # col.append(btn4)
    row.tk_ref.place(x=1, y=1)
    app.run()
