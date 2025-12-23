#!/usr/bin/env python3

from validator import SudokuValidator
from solver import SudokuSolver


def _format_grid_row(grid, row_index):
    """
    Format a single row with spacing and separators.

    Args:
        grid: Sudoku grid
        row_index: Row to format (0-8)
    Returns:
        Formatted row string
    """
    row_str = "│"
    for j in range(9):
        value = grid[row_index, j]
        row_str += f" {value if value != 0 else '.'}"
        if (j + 1) % 3 == 0:
            row_str += " │"
    return row_str


def _get_separator_line():
    """
    Get horizontal separator for 3x3 boxes.

    Returns:
        Separator line string
    """
    return "├───────┼───────┼───────┤"


class Sudoku(object):

    def __init__(self, grid):
        self.grid = grid

    def __str__(self):
        """
        Print the grid.

        Returns:
            Formatted grid string
        """
        lines = ["┌───────┬───────┬───────┐"]

        for i in range(9):
            lines.append(_format_grid_row(self.grid, i))

            if (i + 1) % 3 == 0 and i < 8:
                lines.append(_get_separator_line())

        lines.append("└───────┴───────┴───────┘")
        return "\n".join(lines)

    def solve(self):
        """
        Solve the puzzle using backtracking.

        Returns:
            True if solved, False otherwise
        """
        validator = SudokuValidator()
        solver = SudokuSolver(validator)
        return solver.solve(self.grid)


def run_sudoku(input):
    sudoku = Sudoku(input)
    sudoku.solve()
    print(sudoku)
    
    return sudoku.grid


def compare(source, reference):
    for row in range(9):
        for col in range(9):
            if source[row][col] != reference[row][col]:
                return False
    
    return True

