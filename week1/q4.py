def lu_decomposition(A):
    L = [[0, 0, 0] for _ in range(3)]
    U = [[0, 0, 0] for _ in range(3)]

    for i in range(3):
        L[i][i]=1

    for i in range (3):
        U[0][i] = A[0][i]

    for i in range (1, 3):
        L[i][0] = A[i][0] / U[0][0]

    for j in range (1, 3):
        U[1][j] = A[1][j] - L[1][0]*U[0][j]

    U[2][2] = A[2][2] - L[2][0]*U[0][2] - L[2][1]*U[1][2]
    L[2][1] = (A[2][1] - L[2][0] * U[0][1]) / U[1][1]

    return L, U

A = [[1, 0, 1], [4, 4, 4], [2, 2, 4]]
L, U= lu_decomposition(A)

print(L)
print(U)