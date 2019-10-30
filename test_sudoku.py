import pytest

from fixtures import puzzle, solution
from sudoku import Sudoku

sudoku = Sudoku(puzzle)


def test_get_row():
    assert sudoku.get_row(0) == [5, 3, 0, 0, 7, 0, 0, 0, 0]
    assert sudoku.get_row(5) == [7, 0, 0, 0, 2, 0, 0, 0, 6]
    assert sudoku.get_row(8) == [0, 0, 0, 0, 8, 0, 0, 7, 9]
    with pytest.raises(IndexError):
        sudoku.get_row(9)


def test_get_col():
    assert sudoku.get_col(0) == [5, 6, 0, 8, 4, 7, 0, 0, 0]
    assert sudoku.get_col(2) == [0, 0, 8, 0, 0, 0, 0, 0, 0]
    assert sudoku.get_col(5) == [0, 5, 0, 0, 3, 0, 0, 9, 0]
    assert sudoku.get_col(8) == [0, 0, 0, 3, 1, 6, 0, 5, 9]
    with pytest.raises(IndexError):
        sudoku.get_col(9)


def test_get_box():
    assert sudoku.get_box(0, 0) == [5, 3, 0, 6, 0, 0, 0, 9, 8]
    assert sudoku.get_box(5, 5) == [0, 6, 0, 8, 0, 3, 0, 2, 0]
    assert sudoku.get_box(0, 8) == [0, 6, 0, 0, 0, 0, 0, 0, 0]
    assert sudoku.get_box(0, 2) == [5, 3, 0, 6, 0, 0, 0, 9, 8]
    with pytest.raises(IndexError):
        sudoku.get_box(0, 9)


def test_possible_solutions():
    assert sudoku.possible_solutions(0, 0) == [5]
    assert sudoku.possible_solutions(2, 0) == [1, 2, 4]
    assert sudoku.possible_solutions(4, 6) == [3, 5]


def test_is_solved():
    assert sudoku.is_solved() is False
    assert Sudoku(solution).is_solved() is True


def test_solve():
    assert sudoku.puzzle == puzzle
    sudoku.solve()
    assert sudoku.puzzle == solution


def test_validate_unsolved():
    assert Sudoku(puzzle).validate() is False


def test_validate_solved():
    assert Sudoku(solution).validate() is True
