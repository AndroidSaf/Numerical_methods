# Simple_iteration_numerical_method

import numpy as np

def d_max(X_1, X_2, n):
    max = 0
    for i in range(n):
        m = np.abs(X_1[i] - X_2[i])
        if m > max:
            max = m
    return max

def Simple_iteration_method(A, B, n):
    epsilon = np.exp(-36)
    A_new = np.zeros((n, n))
    B_new = np.zeros(n)
    C = np.zeros(n)

    for i in range(n):
        B_new[i] = B[i] / A[i, i]
        for j in range(n):
            if i != j:
                A_new[i, j] = -1 * A[i, j] / A[i, i]

    a_max = a = 0
    for i in range(n):
        for j in range(n):
            a += np.abs(A_new[i, j])
        if a > a_max:
            a_max = a
        a = 0

    X_1 = B_new + np.dot(A_new, C)
    delta = 1
    while delta > np.abs((1 - a_max) * epsilon / a_max):
        X_2 = X_1
        X_1 = B_new + np.dot(A_new, X_2)
        delta = d_max(X_1, X_2, n)

    print("X' = \n", X_1)
    return X_1