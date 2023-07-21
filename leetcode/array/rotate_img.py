def rotate(matrix):
    left, right = 0, len(matrix) - 1
    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            topLeft = matrix[top][left + i]
            # move bottom left to top right
            matrix[top][left + i] = matrix[bottom - i][left]
            # move bottom right to bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # move matrix top right to bottom left
            matrix[bottom][right - i] = matrix[top + i][right]
            # since top left is not free, top left can now be equal to topleft
            matrix[top + i][right] = topLeft
        right -= 1
        left += 1


print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def rotate1(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):  # Iterate over the rows
        for j in range(i, n):  # Iterate over the columns starting from the current row 'i'
            # Swap the elements at positions (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:  # Iterate over each row in the matrix
        row.reverse()  # Reverse the elements in the current row
