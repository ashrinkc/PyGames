from tkinter import *
import random
import setting


class Cell:
    all = []
    cell_count = setting.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.cell_btn_object = None
        self.x = x
        self.y = y
        # append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
        )
        btn.bind('<Button-1>', self.left_click_actions)  # left click
        btn.bind('<Button-3>', self.right_click_actions)  # right click
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg="black",
            fg='white',
            text=f"Cells left:{Cell.cell_count}",
            width=12,
            height=4,
            font=("", 30)
        )
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):
        if (self.is_mine):
            self.show_mine()
        else:
            if self.surrounded_cells_length_mines == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

    def get_cell_by_axis(self, x, y):
        # return cell object based of value of x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property  # to make it read only
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y-1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y+1),
            self.get_cell_by_axis(self.x, self.y-1),
            self.get_cell_by_axis(self.x + 1, self.y-1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y+1),
            self.get_cell_by_axis(self.x, self.y+1),
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_length_mines(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(
                text=self.surrounded_cells_length_mines)
            # replace text of cell count label
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells left:{Cell.cell_count}"
                )
        # mark the cell as opened
        self.is_opened = True

    def show_mine(self):
        # logic to display player lost
        self.cell_btn_object.configure(bg="red")

    def right_click_actions(self, event):
        self.cell_btn_object.configure(bg="blue")

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, setting.MINES_COUNT)
        for pc in picked_cells:
            pc.is_mine = True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"
