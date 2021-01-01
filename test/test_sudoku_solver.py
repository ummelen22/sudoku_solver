from sudoku_solver.src.solve_sudoku import is_valid, _solve_sudoku


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

SOLUTION = [
    [1, 2, 3, 7, 8, 9, 4, 5, 6],
    [4, 5, 6, 1, 2, 3, 7, 8, 9],
    [7, 8, 9, 4, 5, 6, 1, 2, 3],
    [2, 3, 1, 8, 9, 7, 5, 6, 4],
    [5, 6, 4, 2, 3, 1, 8, 9, 7],
    [8, 9, 7, 5, 6, 4, 2, 3, 1],
    [3, 1, 2, 9, 7, 8, 6, 4, 5],
    [6, 4, 5, 3, 1, 2, 9, 7, 8],
    [9, 7, 8, 6, 4, 5, 3, 1, 2],
]


def test_is_valid():
    """ Test the is_valid function. """

    # Given, I have an unsolved sudoku puzzle
    sudoku = SUDOKU

    # When I ask for a prefilled element with its prefilled value
    prefilled_location = [0, 0]
    prefilled_value = 1

    # Then the validation method should return True
    assert (
        is_valid(sudoku, prefilled_location[0], prefilled_location[1], prefilled_value) is True
    ), "Providing a prefilled element of the sudoku with its prefilled value, the validation method should return True"

    # When I ask for a prefilled element with a different value
    prefilled_location = [0, 0]
    invalid_value = 6

    # Then the validation method should return False
    assert (
        is_valid(sudoku, prefilled_location[0], prefilled_location[1], invalid_value) is False
    ), "Providing a prefilled element of the sudoku with a different value, the validation method should return False"

    # When I ask for an unfilled element with a valid option
    unfilled_location = [1, 1]
    valid_option = 5

    # Then the validation method should return True
    assert (
        is_valid(sudoku, unfilled_location[0], unfilled_location[1], valid_option) is True
    ), "Providing an unfilled element of the sudoku with a valid option, the validation method should return True"

    # When I ask for an unfilled element with an invalid option because the number exists in the row
    unfilled_location = [1, 1]
    invalid_row_option = 2

    # Then the validation method should return False
    assert (
        is_valid(sudoku, unfilled_location[0], unfilled_location[1], invalid_row_option) is False
    ), "Providing an unfilled element of the sudoku with an invalid row option, the validation method should return False"

    # When I ask for an unfilled element with an invalid option because the number exists in the column
    unfilled_location = [3, 0]
    invalid_column_option = 3

    # Then the validation method should return False
    assert (
        is_valid(sudoku, unfilled_location[0], unfilled_location[1], invalid_column_option) is False
    ), "Providing an unfilled element of the sudoku with an invalid column option, the validation method should return False"

    # When I ask for an unfilled element with an invalid option because the number exists in the box
    unfilled_location = [0, 3]
    invalid_box_option = 2

    # Then the validation method should return False
    assert (
        is_valid(sudoku, unfilled_location[0], unfilled_location[1], invalid_box_option) is False
    ), "Providing an unfilled element of the sudoku with an invalid box option, the validation method should return False"


def test_sudoku_solver():
    """ Tests whether the solver correctly solves a sudoku """
    _solve_sudoku(sudoku=SUDOKU)
    assert SUDOKU == SOLUTION