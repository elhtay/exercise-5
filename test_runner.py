#!/usr/bin/env python3

import numpy as np
from sudoku import Sudoku, compare

# Test cases
tests = [
    ("input-0.npy", "reference-0.npy"),
    ("input-1.npy", "reference-1.npy"),
    ("input-2.npy", "reference-2.npy"),
    ("input-3.npy", None), 
]

passed = 0
for i, (input_file, ref_file) in enumerate(tests):
    print(f"\n{'='*40}")
    print(f"Test {i}: {input_file}")
    print(f"{'='*40}")
    
    # Load and solve
    sudoku = Sudoku(np.load(input_file))
    print("Input:")
    print(sudoku)
    
    if sudoku.solve():
        print("\nSolved:")
        print(sudoku)
        
        # Check against reference if available
        if ref_file:
            if compare(sudoku.grid, np.load(ref_file)):
                print("✓ PASSED")
                passed += 1
            else:
                print("✗ FAILED")
        else:
            print("✓ COMPLETED") 
            passed += 1
    else:
        print("✗ No solution found")

print(f"\n{'='*40}")
print(f"Results: {passed}/{len(tests)} passed")
print(f"{'='*40}")
