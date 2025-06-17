def gaussian_elimination(A, b):
    x = len(A)
    
    for i in range(0, x):
        A[i].append(b[i])

    for i in range(0, x):
        if A[i][i]==0:
            for j in range(i+1, x):
                if A[j][i] !=0:
                    A[i],A[j] = A[j], A[i]
                    break
        pivot = A[i][i]
        if pivot !=0:
            for k in range(i, x+1):
                A[i][k] = A[i][k]/pivot

        for j in range(i+1, x):
            n = A[j][i]
            for k in range(i, x+1):
                A[j][k] = A[j][k] - (A[i][k]*n)

    return A


A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
b = [8, -11, -3]

x =gaussian_elimination(A, b)
print(x)





