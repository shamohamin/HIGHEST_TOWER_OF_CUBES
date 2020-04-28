import tkinter as tk
from src.logic.cube import Cube
import copy
import random
import time


class UI(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.colors = ["red", "blue", "green", "purple", "yellow", "white"]

    def draw(self, arr):
        x_pos, y_pos, last_weight = 200, 200, arr[0].weight
        for x in arr:
            time.sleep(1)
            self._make_rectangle(x_pos, y_pos, 50 / x.weight)
            if last_weight != x.weight:
                last_weight = x.weight
                y_pos -= 50
            self._packing()

    def show_perm(self, x):
        time.sleep(1)
        self._make_rectangle(200, 200, 20 * x.weight)
        self._packing()
        self.canvas.delete("all")

    def _packing(self):
        self.canvas.update()
        self.canvas.pack()
        self.pack()

    def _make_rectangle(self, x, y, wieght):
        # make back
        self.canvas.create_rectangle(x, y, x + wieght, y + wieght, fill=self._choose_color())
        # make left
        self.canvas.create_polygon([x, y, x - 20, y + 20, x - 20, y + 20 + wieght,
                                        x, y + wieght], fill=self._choose_color(), outline="red")
        # make up
        self.canvas.create_polygon([x, y, x - 20, y + 20, x - 20 + wieght,
                                        y + 20, x + wieght, y], fill=self._choose_color(), outline="red")
        # make right
        self.canvas.create_polygon([x + wieght, y, x - 20 + wieght, y + 20, x - 20 + wieght, y + 20 + wieght,
                                        x + wieght, y + wieght], outline="red", fill=self._choose_color())
        # make right
        self.canvas.create_polygon([x + wieght, y + wieght, x, y + wieght, x - 20,
                                        y + 20 + wieght, x - 20 + wieght,
                                        y + wieght + 20], outline="red", fill=self._choose_color())
        # make front
        self.canvas.create_rectangle(x - 20, y + 20, x + wieght - 20,
                                        y + wieght + 20, outline="red", fill=self._choose_color())

    def _choose_color(self):
        return self.colors[random.randint(0, len(self.colors) - 1)]


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
    ui = UI(root)
    arr = [Cube(1), Cube(2), Cube(3)]
    permutation(arr, ui)
    # ui.draw(arr)
    ui.mainloop()


