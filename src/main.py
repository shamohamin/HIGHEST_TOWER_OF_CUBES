import tkinter as tk
from src.logic.cube import Cube
from src.logic.ui import UI
from src.logic.tower import permutation, make_highest_tower

if __name__ == '__main__':
    root = tk.Tk()
    root.title("TOWER OF CUBES")
    ui = UI(root)
    cube = Cube(7)
    cube.left, cube.right, cube.up, cube.down, cube.front = 7, 7, 7, 7, 7
    arr = [Cube(1), Cube(2), Cube(3), Cube(4), Cube(5), cube, Cube(6)]
    permutation(arr, ui)
    make_highest_tower(arr, ui)
    # ui.draw(arr)
    ui.mainloop()


