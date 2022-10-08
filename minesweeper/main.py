from tkinter import *
from cell import Cell
import setting
import utils
root = Tk()
# override the setting of the window
root.configure(bg="black")
root.geometry(f'{setting.WIDTH}x{setting.HEIGHT}')
root.title("Minesweeper")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg="black",
    width=setting.WIDTH,
    height=utils.height_perct(25)
)

top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg="black",
    width=utils.width_prct(25),
    height=utils.height_perct(75)
)

left_frame.place(x=0, y=utils.height_perct(25))

center_frame = Frame(
    root,
    bg="black",
    width=utils.width_prct(75),
    height=utils.height_perct(75)
)

center_frame.place(x=utils.width_prct(25), y=utils.height_perct(25))

for x in range(setting.GRID_SIZE):
    for y in range(setting.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x, row=y)

# call the label from cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()
# run the window
root.mainloop()
