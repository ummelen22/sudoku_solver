""" Solver for sudoku puzzels """


def is_valid(sudoku, x, y, number):
    if sudoku[x][y] != 0:
        if sudoku[x][y] == number:
            return True
        else:
            return False
    return False
