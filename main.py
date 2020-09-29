# Main program for solving SLAE

import numpy as np
import random as rd
import Gauss_method as f_1
import Sweep_method as f_2
import Simple_iteration_method as f_3

# import Simple_iteration_method as f_3

l = 'yes'

def get_B(A, X):
    B = np.dot(A, X)
    return B

def diag_max(C):
    for i in range(n):
        for j in range(n):
            if i == j:
                C[i, j] = rd.random() + 100
            else:
                C[i, j] = rd.random()
    return C

def three_diag_matrix(C):
    for i in range(n):
        for j in range(n):
            if i == j:
                C[i, j] = rd.random()
            elif np.abs(i - j) == 1:
                C[i, j] = rd.random()
    return C

while l == 'yes':

    print("------------------------------------------")
    print("Gauss_method")
    n = int(input("Enter the number of equations: \n"))
    A = np.array([rd.random() for i in range(n ** 2)])
    A = A.reshape(n, n)
    print("A = \n", A)
    X = np.array([rd.random() for i in range(n)])
    print("X = \n", X)
    B = get_B(A, X)
    print("B = \n", B)
    print("dX = \n", X - f_1.Gauss_method(A, B, n))

    print("------------------------------------------")
    print("Sweep_method")
    n = int(input("Enter the number of equations: \n"))
    C = np.zeros((n, n))
    A = three_diag_matrix(C)
    print("A = \n", A)
    print("X = \n", X)
    B = get_B(A, X)
    print("B = \n", B)
    print("dX = \n", X - f_2.Sweep_method(A, B, n))

    print("------------------------------------------")
    print("Simple_iteration_method")
    n = int(input("Enter the number of equations: \n"))
    C = np.zeros((n, n))
    A = diag_max(C)
    print("A = \n", A)
    print("X = \n", X)
    B = get_B(A, X)
    print("B = \n", B)
    print("dX = \n", X - f_3.Simple_iteration_method(A,B,n))

    print("Try again?")
    l = input()

print("Thank you for attention!")
