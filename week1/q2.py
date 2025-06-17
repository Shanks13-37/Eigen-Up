def matrix_multiply(A, B):
    m = len(A)
    n = len(A[0])
    o = len(B)
    p = len(B[0])

    if not n==o:
        return -1
    
    C = [[0 for _ in range(0, p)] for _ in range(0, m)]

    for i in range (0, m):
        for j in range (0, p):
            for k in range (0, n):
                C[i][j] += A[i][k]*B[k][j]

    return C
    

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

c = matrix_multiply(A, B)

print(c)