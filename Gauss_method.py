# Gauss numerical method

def Gauss_method(A, B, n):
    for k in range(n - 1):
        for i in range(k + 1, n):
            b = A[i, k] / A[k, k]
            for j in range(k, n):
                A[k, j] *= b
            B[k] *= b
            for j in range(k, n):
                A[i, j] -= A[k, j]
            B[i] -= B[k]

    k = n - 1
    while k > 0:
        i = k - 1
        while i >= 0:
            b = A[i, k] / A[k, k]
            j = k
            while j >= 0:
                A[k, j] *= b
                j -= 1
            B[k] *= b
            j = k
            while j >= 0:
                A[i, j] -= A[k, j]
                j -= 1
            B[i] -= B[k]
            i -= 1
        k -= 1

    for i in range(n):
        for j in range(n):
            if i != j:
                A[i, j] = 0
            else:
                B[i] /= A[i, j]
                A[i, j] /= A[i, j]
    new_X = B

    print("X' = \n", new_X)
    return new_X
