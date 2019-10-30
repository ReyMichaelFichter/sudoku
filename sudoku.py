import copy

boxes = [
    {"cols": range(0, 3), "rows": range(0, 3)},
    {"cols": range(0, 3), "rows": range(3, 6)},
    {"cols": range(0, 3), "rows": range(6, 9)},
    {"cols": range(3, 6), "rows": range(0, 3)},
    {"cols": range(3, 6), "rows": range(3, 6)},
    {"cols": range(3, 6), "rows": range(6, 9)},
    {"cols": range(6, 9), "rows": range(0, 3)},
    {"cols": range(6, 9), "rows": range(3, 6)},
    {"cols": range(6, 9), "rows": range(6, 9)},
]


class Sudoku:
    def __init__(self, puzzle):
        self.puzzle = copy.deepcopy(puzzle)

    def get_row(self, row):
        return self.puzzle[row]

    def get_col(self, col):
        return [self.puzzle[n][col] for n in range(9)]

    def get_box(self, col, row):
        box = [
            box for box in boxes if row in box["rows"] if col in box["cols"]
        ][0]
        return [
            self.puzzle[row][col] for row in box["rows"] for col in box["cols"]
        ]

    def possible_solutions(self, col, row):
        if self.puzzle[row][col] != 0:
            return [self.puzzle[row][col]]
        return list(
            {1, 2, 3, 4, 5, 6, 7, 8, 9}
            - (
                set(self.get_row(row))
                | set(self.get_col(col))
                | set(self.get_box(col, row))
            )
        )

    def is_solved(self):
        return all([0 not in row for row in self.puzzle])

    def solve(self):
        while not self.is_solved():
            for row in range(9):
                for col in range(9):
                    p = self.possible_solutions(col, row)
                    if len(p) == 1:
                        self.puzzle[row][col] = list(p)[0]

    def validate(self):
        if not self.is_solved():
            return False
        for i in range(9):
            if sorted(self.get_row(i)) != list(range(1, 10)):
                return False
            if sorted(self.get_col(i)) != list(range(1, 10)):
                return False
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if sorted(self.get_box(col, row)) != list(range(1, 10)):
                    return False
        return True
