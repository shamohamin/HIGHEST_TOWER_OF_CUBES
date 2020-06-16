import tkinter as tk
from Ui.ui import UI
from Ui.welcome import WelcomeFrame
from logic.cube import Cube
from logic.tower import permutation, make_highest_tower


class Controller(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.frames = {}
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.title("TOWER OF CUBES")

        for F in (UI, WelcomeFrame):
            frame = F(container, self)
            self.frames[F] = frame

        self.show_frames(WelcomeFrame)

    def show_frames(self, frame):
        f = self.frames[frame]
        f.tkraise()

    def starter(self):
        ui = self.frames[UI]
        ui.tkraise()
        cube = Cube(6)
        cube.left, cube.right, cube.up, cube.down, cube.front = 7, 7, 7, 7, 7
        cube1 = Cube(1)
        cube1.left, cube1.right = 1, 1
        arr = [cube1, Cube(2), Cube(3), Cube(4), Cube(5), cube]
        permutation(arr, ui)
        make_highest_tower(arr, ui)
