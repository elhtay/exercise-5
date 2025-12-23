import numpy as np


class SudokuValidator:
    """Checks if placements follow Sudoku rules."""
    
    GRID_SIZE = 9
    BOX_SIZE = 3
    EMPTY_CELL = 0
    
    @staticmethod
    def is_valid_placement(grid: np.ndarray, row: int, col: int, num: int) -> bool:
        """
        Check if placement is valid.
        
        Args:
            grid: Sudoku grid
            row: Row index (0-8)
            col: Column index (0-8)
            num: Number to place (1-9)
        Returns:
            True if valid, False otherwise
        """
  
        if num in grid[row]:
            return False
        

        if num in grid[:, col]:
            return False
        
        # Check 3x3 box constraint
        box_row_start = (row // SudokuValidator.BOX_SIZE) * SudokuValidator.BOX_SIZE
        box_col_start = (col // SudokuValidator.BOX_SIZE) * SudokuValidator.BOX_SIZE
        
        box = grid[box_row_start:box_row_start + SudokuValidator.BOX_SIZE,
                   box_col_start:box_col_start + SudokuValidator.BOX_SIZE]
        
        if num in box:
            return False
        
        return True
