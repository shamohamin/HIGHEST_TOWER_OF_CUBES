import tkinter as tk
from src.logic.cube import Cube
from src.logic.ui import UI
import copy


def permutation(arr, ui):
    arr_holder = arr.copy()
    for c in arr_holder:
        hold = copy.copy(c)

        ui.show_perm(c)
        arr.append(Cube(c.weight, right=hold.down, up=hold.left, down=hold.right, left=hold.up, back=hold.back,
                        front=hold.front))
        ui.show_perm(arr[-1])

        arr.append(Cube(c.weight, right=hold.up, up=hold.right, down=hold.left, left=hold.down, back=hold.back,
                        front=hold.front))
        ui.show_perm(arr[-1])
        arr.append(Cube(c.weight, right=hold.right, up=hold.front, down=hold.back, left=hold.left, back=hold.down,
                        front=hold.up))
        ui.show_perm(arr[-1])
        arr.append(Cube(c.weight, right=hold.right, up=hold.back, down=hold.front, left=hold.left, back=hold.up,
                        front=hold.down))
        ui.show_perm(arr[-1])
        arr.append(Cube(c.weight, right=hold.right, up=hold.down, down=hold.up, left=hold.left, back=hold.back,
                        front=hold.front))
        ui.show_perm(arr[-1])


def make_highest_tower(arr):
    pass


if __name__ == '__main__':
    root = tk.Tk()
    root.title("TOWER OF CUBES")
    ui = UI(root)
    arr = [Cube(1), Cube(2), Cube(3)]
    permutation(arr, ui)
    # ui.draw(arr)
    ui.mainloop()


