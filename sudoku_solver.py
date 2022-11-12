from pulp import *
from numpy import np 


def get_sudoku_frame():
    return  np.kron(np.ones((3,3)),np.zeros((3,3)))
