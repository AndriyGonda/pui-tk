from pui_tk import Application
from pui_tk.widgets.layouts import Column, Grid
from pui_tk.widgets import Label
from pui_tk.types import Cursor, Relief, Justify


def label_cursors(base) -> Grid:
    row = Grid(base)
    for index, cursor_type in enumerate(Cursor):
        label = Label(row, text=str(cursor_type.value), cursor=cursor_type, bg_color=f'#aaa')
        row.add(0, index, label, margin_x=5)
    return row


def label_relief(base) -> Grid:
    row = Grid(base)
    for index, relief_type in enumerate(Relief):
        label = Label(row, text=str(relief_type.value), relief=relief_type)
        row.add(0, index, label, margin_x=5)
    return row


def label_justify(base) -> Grid:
    row = Grid(base)
    for index, justify_type in enumerate(Justify):
        label = Label(
            row,
            text=f'multiline\ntext\n' + str(justify_type.value),
            justify=justify_type
        )
        row.add(0, index, label, margin_x=5)
    return row


def wrap_length_example(base) -> Grid:
    text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Vivamus tellus tellus, sodales sit amet dapibus sed, dapibus ac erat.
    Maecenas quis convallis justo, id fringilla mi.
    """
    row = Grid(base)
    wrap_length = [50, 100, 200, 300, 400]
    for index, length in enumerate(wrap_length):
        label = Label(
            row,
            text=f'({length} px)\n' + text,
            wrap_len=length,
            justify=Justify.LEFT
        )
        row.add(0, index, label, margin_x=5)
    return row


if __name__ == '__main__':
    app = Application('Label Usage')
    app.set_min_size(850, 600)
    col = Column(app)

    title_cursors = Label(col, text='Move cursor on label with title for view cursor', font=['bold'])
    r_label_cursors = label_cursors(col)
    col.append(title_cursors, fill=True, expand=True)
    col.append(r_label_cursors, fill=True, expand=True)

    title_reliefs = Label(col, text='Available label reliefs', font=['bold'])
    label_reliefs = label_relief(col)
    col.append(title_reliefs, fill=True, expand=True)
    col.append(label_reliefs, fill=True, expand=True)

    title_justify = Label(col, text='Available justify multiline text examples', font=['bold'])
    col.append(title_justify, fill=True, expand=True)
    col.append(label_justify(col), fill=True, expand=True)

    col.append(Label(col, text='Label wrap_len examples', font=['bold']))
    col.append(wrap_length_example(col))

    col.tk_ref.pack()
    app.run()
