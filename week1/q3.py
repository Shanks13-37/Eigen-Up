def inverse_2x2(matrix):
    matrix = [[matrix[0][0], matrix[0][1], 1, 0],
              [matrix[1][0], matrix[1][1], 0, 1]] 

    if matrix[0][0]!=1:
        x = matrix[0][0]
        matrix /= x

    x = matrix[1][0]
    for i in range (4):
        matrix[1][i] -= (matrix[0][i]*x)

    x = matrix[1][1]
    for i in range (4):
        matrix[1][i] /= x
    
    x = matrix[0][1] 
    for i in range (4):
        matrix[0][i] -= (matrix[1][i]*x)


    matrix = [[matrix[0][2], matrix[0][3]], 
               [matrix[1][2], matrix[1][3]]]

    return matrix



A = [[1, 2],
     [3, 4]]

B = inverse_2x2(A)

print(B)