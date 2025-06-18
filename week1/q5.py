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

def solve_lu(A, b):
    # Use LU decomposition to solve Ax = b
    L, U= lu_decomposition(A)
    y= [0,0,0]
    for i in range(3):
            z = sum(L[i][j] * y[j] for j in range(i))
            y[i] = b[i] -z
    x= [0, 0, 0]
    for i in reversed(range(3)):
            z = y[i] - sum(U[i][j]*x[j] for j in range(i+1, 3))
            x[i] = z/U[i][i]

    return x, y


A = [[1, 0, 1], [4, 4, 4], [2, 2, 4]]
b = [6, 24, 18]

x, y= solve_lu(A, b)

print(f"Solution x: {x}")
print(f"E y: {y}")