from  sudoku_solver import *

def test_get_sudoku_frame():
    sdk_frame = get_sudoku_frame() 
    assert sdk_frame.shape == (9,9)