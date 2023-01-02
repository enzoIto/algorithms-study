
def rotate(matrix):
  n = len(matrix)

  # transpose matrix
  for i in range(n):
    for j in range(i, n):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

  # reverse each row
  for i in range(n):
    matrix[i] = matrix[i][::-1]