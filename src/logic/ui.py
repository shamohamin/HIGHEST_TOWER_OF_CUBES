import tkinter as tk
import time
import random


class UI(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=600, height=600)
        self.colors_dic = {
            1: "red",
            2: "blue",
            3: "green",
            4: "purple",
            5: "yellow",
            6: "white",
            7: "orange"
        }
        self.colors = ["white", "purple", "yellow", "blue", "green", "red"]

    def draw(self, arr):
        x_pos, y_pos, last_weight = 280, 450, arr[0].weight
        for x in arr:
            time.sleep(1)
            self._make_rectangle(x_pos, y_pos, 20 * x.weight, x)

            y_pos -= 20 * x.weight
            x_pos += 10

            self._packing()

    def show_perm(self, x):
        time.sleep(0.25)
        self._make_rectangle(200, 200, 20 * x.weight, x)
        self._packing()
        self.canvas.delete("all")

    def _packing(self):
        self.canvas.update()
        self.canvas.pack()
        self.pack()

    def show_error(self, error_msg):
        tk.Label(self, text=error_msg).pack()
        self.pack()

    def _make_rectangle(self, x, y, wieght, cube):
        # make back
        self.canvas.create_rectangle(x, y, x + wieght, y + wieght, fill=self.colors_dic[cube.back])
        # make left
        self.canvas.create_polygon([x, y, x - 20, y + 20, x - 20, y + 20 + wieght,
                                        x, y + wieght], fill=self.colors_dic[cube.left], outline="red")
        # make up
        self.canvas.create_polygon([x, y, x - 20, y + 20, x - 20 + wieght,
                                        y + 20, x + wieght, y], fill=self.colors_dic[cube.up], outline="red")
        # make right
        self.canvas.create_polygon([x + wieght, y, x - 20 + wieght, y + 20, x - 20 + wieght, y + 20 + wieght,
                                        x + wieght, y + wieght], outline="red", fill=self.colors_dic[cube.right])
        # make right
        self.canvas.create_polygon([x + wieght, y + wieght, x, y + wieght, x - 20,
                                        y + 20 + wieght, x - 20 + wieght,
                                        y + wieght + 20], outline="red", fill=self.colors_dic[cube.down])
        # make front
        self.canvas.create_rectangle(x - 20, y + 20, x + wieght - 20,
                                        y + wieght + 20, outline="red", fill=self.colors_dic[cube.front])

    def _choose_color(self):
        return self.colors[random.randint(0, len(self.colors) - 1)]
