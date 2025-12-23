from typing import Optional, Tuple
import numpy as np
from validator import SudokuValidator


class SudokuSolver:
    """Recursive backtracking solver."""
    
    def __init__(self, validator: SudokuValidator):
        self.validator = validator
    
    def solve(self, grid: np.ndarray) -> bool:
        """
        Solve puzzle by filling empty cells.
        
        Args:
            grid: Grid to solve
        Returns:
            True if solved, False otherwise
        """
        empty_cell = self._find_empty_cell(grid)
        
        if empty_cell is None:
            return True
        
        row, col = empty_cell
        
        for num in range(1, 10):
            if self.validator.is_valid_placement(grid, row, col, num):
                grid[row, col] = num
                
                if self.solve(grid):
                    return True
                
                # Backtrack
                grid[row, col] = SudokuValidator.EMPTY_CELL

        return False

    @staticmethod
    def _find_empty_cell(grid: np.ndarray) -> Optional[Tuple[int, int]]:
        """
        Find next empty cell.
        
        Args:
            grid: Grid to search
        Returns:
            (row, col) tuple or None if full
        """
        for row in range(SudokuValidator.GRID_SIZE):
            for col in range(SudokuValidator.GRID_SIZE):
                if grid[row, col] == SudokuValidator.EMPTY_CELL:
                    return (row, col)
        return None
