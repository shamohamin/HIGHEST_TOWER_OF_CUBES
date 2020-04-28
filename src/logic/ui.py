import tkinter as tk
import time
import random


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
