""" Solver for sudoku puzzels """

import random
import time

INIT_SUDOKU = [
    [1, 0, 0, 0, 0, 0, 0, 0, 6],  # .         y
    [0, 0, 6, 0, 2, 0, 7, 0, 0],  # .------------------>
    [7, 8, 9, 4, 5, 0, 1, 0, 3],  # |
    [0, 0, 0, 8, 0, 7, 0, 0, 4],  # |
    [0, 0, 0, 0, 3, 0, 0, 0, 0],  # |
    [0, 9, 0, 0, 0, 4, 2, 0, 1],  # x|
    [3, 1, 2, 9, 7, 0, 0, 4, 0],  # |
    [0, 4, 0, 0, 1, 2, 0, 7, 8],  # |
    [9, 0, 8, 0, 0, 0, 0, 0, 0],  # V
]

SUDOKU = [
    [1, 0, 0, 0, 0, 0, 0, 0, 6],  # .         y
    [0, 0, 6, 0, 2, 0, 7, 0, 0],  # .------------------>
    [7, 8, 9, 4, 5, 0, 1, 0, 3],  # |
    [0, 0, 0, 8, 0, 7, 0, 0, 4],  # |
    [0, 0, 0, 0, 3, 0, 0, 0, 0],  # |
    [0, 9, 0, 0, 0, 4, 2, 0, 1],  # x|
    [3, 1, 2, 9, 7, 0, 0, 4, 0],  # |
    [0, 4, 0, 0, 1, 2, 0, 7, 8],  # |
    [9, 0, 8, 0, 0, 0, 0, 0, 0],  # V
]


def is_valid(sudoku, x, y, number):
    """ Returns whether the provided number and location are a valid combination for the sudoku """
    if sudoku[x][y] not in range(10):
        raise ValueError(
            f"The current value at [{x}, {y}] is {sudoku[x][y]}, which does not lay within the allowed sudoku values of 1-9"
        )

    if number not in range(1, 10):
        raise ValueError(f"The suggested number {number} does not lay within the allowed sudoku values of 1-9")

    if sudoku[x][y] != 0:
        if sudoku[x][y] == number:
            return True
        else:
            return False

    # Check whether the number exists in the row
    if number in sudoku[x]:
        return False

    # Check whether the number exists in the column
    if number in [row[y] for row in sudoku]:
        return False

    # Check whether the number exists in the box
    search_range = dict()
    search_range['x'] = [(x // 3) * 3 + i for i in range(3)]
    search_range['y'] = [(y // 3) * 3 + i for i in range(3)]

    for search_x in search_range['x']:
        for search_y in search_range['y']:
            if sudoku[search_x][search_y] == number:
                return False

    return True


def find_empty_cell(grid):
    """ Returns the first empty cell it finds in a 2D grid """
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 0:
                return x, y

    return None


def _solve_sudoku_brute_force(sudoku):
    """ Brute force solver for sudoku's """
    while True:
        no_valid_numbers = False
        for x in range(len(sudoku)):
            for y in range(len(sudoku[0])):
                print(x, y)
                if sudoku[x][y] == 0:
                    valid_numbers = []

                    for number in range(1, 10):
                        if is_valid(sudoku, x, y, number):
                            valid_numbers.append(number)

                    if not valid_numbers:
                        print_sudoku_human_readable(sudoku)
                        sudoku = INIT_SUDOKU
                        print_sudoku_human_readable(sudoku)
                        input("continue?")
                        no_valid_numbers = True
                        break
                    else:
                        i = random.randint(0, len(valid_numbers) - 1)
                        number = valid_numbers[i]
                        sudoku[x][y] = number
                else:
                    continue
            if no_valid_numbers:
                break
        if not find_empty_cell(sudoku):
            return True


def _solve_sudoku(sudoku):
    """ Backtracking solver for sudoku's """
    empty_cell = find_empty_cell(sudoku)
    if not empty_cell:
        return True

    x, y = empty_cell
    for number in range(1, 10):
        if is_valid(sudoku, x, y, number):
            sudoku[x][y] = number
            if _solve_sudoku(sudoku):
                return True
            sudoku[x][y] = 0

    return False


def print_sudoku_human_readable(sudoku):
    """ Prints the sudoku in a pretty fashion such that it is human readable """
    sudoku_readable = []
    horizontal = "+ - - - + - - - + - - - +"
    sudoku_readable.append(horizontal)
    for n, row in enumerate(sudoku):
        row_string_list = [str(num) for num in row]
        for i in [0, 4, 8, 12]:
            row_string_list.insert(i, "|")
        sudoku_readable.append(" ".join(row_string_list))
        if n in [2, 5, 8]:
            sudoku_readable.append(horizontal)
    for row in sudoku_readable:
        print(row)


if __name__ == "__main__":
    print_sudoku_human_readable(SUDOKU)
    start_time = time.time()
    _solve_sudoku_brute_force(SUDOKU)
    end_time = time.time()
    print("-"*50)
    print_sudoku_human_readable(SUDOKU)
    print(f"time spent: {end_time - start_time} sec")
