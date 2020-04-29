import tkinter as tk
from src.logic.cube import Cube
from src.logic.ui import UI
from src.logic.tower import permutation, make_highest_tower

if __name__ == '__main__':
    root = tk.Tk()
    root.title("TOWER OF CUBES")
    ui = UI(root)
    arr = [Cube(1), Cube(2), Cube(3)]
    permutation(arr, ui)
    make_highest_tower(arr, ui)
    # ui.draw(arr)
    ui.mainloop()


