import copy
from src.logic.cube import Cube


def permutation(arr: list, ui):
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


def make_highest_tower(arr: list, ui):
    sol, memory = list(), {}
    arr = sorted(arr, key=lambda cube: cube.weight, reverse=False)

    try:
        # bottom up manner
        for (i, x) in enumerate(arr):
            bottom_cube, hold_possible_towers = x, [x]
            for j in range(i - 1, -1, -1):
                if memory.get(hashing(arr[j])) is None:
                    if bottom_cube.weight > arr[j].weight and bottom_cube.up == arr[j].down:
                        hold_possible_towers.append(arr[j])
                        bottom_cube = arr[j]
                else:
                    memoize = memory.get(hashing(arr[j]))
                    # copy memoize method
                    for y in memoize:
                        if bottom_cube.weight > y.weight:
                            hold_possible_towers.append(y)
                    break
            memory[hashing(hold_possible_towers[0])] = hold_possible_towers
            sol.append(hold_possible_towers)
    except IndexError:
        ui.show_error("Index out of bounds")
    except StopIteration:
        pass
    except KeyError:
        pass
    else:
        for x in sol:
            print(x)

    ui.draw(sol[-1])


def hashing(cube):
    return str(cube.up) + str(cube.down) + str(cube.weight)
