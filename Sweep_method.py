# Sweep_numerical_method

import numpy as np

def Sweep_method(A, B, n):
    alpha = np.zeros(n - 1)
    beta = np.zeros(n)
    A_two_diag = np.eye(n)
    alpha[0] = -A[0, 1] / A[0, 0]
    beta[0] = B[0] / A[0, 0]
    A_two_diag[0, 1] = alpha[0]
    for i in range(n - 1):
        for j in range(n - 1):
            if j - i == 1:
                alpha[i + 1] = -A[i + 1, j + 1] / (A[i + 1, i + 1] + A[j, i] * alpha[i])
                A_two_diag[i + 1, j + 1] = alpha[i + 1]

    for i in range(n):
        for j in range(n):
            if j - i == 1:
                beta[i + 1] = (B[i + 1] - A[j, i] * beta[i]) / (A[i + 1, i + 1] + A[j, i] * alpha[i])

    k = n - 1
    while k > 0:
        beta[k - 1] += beta[k] * A_two_diag[k - 1, k]
        A_two_diag[k - 1, k] -= A_two_diag[k, k] * A_two_diag[k - 1, k]
        k -= 1

    print("X' = \n", beta)
    return beta