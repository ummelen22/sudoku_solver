""" Solver for sudoku puzzels """
import sys


def is_valid(sudoku, x, y, number):
    """ Returns whether the provided number and location are a valid combination for the sudoku """
    if sudoku[x][y] not in range(10):
        raise ValueError(f"The current value at [{x}, {y}] is {sudoku[x][y]}, which does not lay within the allowed sudoku values of 1-9")

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
    return True


def _solve_sudoku(sudoku):
    """ Solves the provided sudoku and returns the solution as a list of lists"""
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                for number in range(1, 10):
                    if is_valid(sudoku, x, y, number):
                        sudoku[x][y] = number
                        _solve_sudoku(sudoku)
                        sudoku[x][y] = 0
                    return
            return sudoku


if __name__ == "__main__":
    sudoku = sys.argv[1:]
    sys.exit(_solve_sudoku(sudoku))
