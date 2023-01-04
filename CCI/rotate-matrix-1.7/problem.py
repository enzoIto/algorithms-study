
def rotate(matrix):
  n = len(matrix)

  # transpose matrix
  for i in range(n):
    for j in range(i, n):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

  # reverse each row
  for i in range(n):
    matrix[i] = matrix[i][::-1]


  return matrix
print(rotate(            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ]))
