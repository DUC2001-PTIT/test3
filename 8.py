def matrixElementsSum(matrix):
    t = 0
    for j in range(0,len(matrix[0])):
        for i in range(0,len(matrix)):
            if( matrix[i][j] == 0):
                break
            else:
                t += matrix[i][j]
    return t