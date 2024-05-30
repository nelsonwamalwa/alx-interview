#!/usr/bin/env python3
"""Rotates an n x n 2D matrix 90 degrees clockwise in-place."""


def rotate_2d_matrix(matrix):
    """
    Rotate the 2D matrix 90 degrees clockwise

    Algorithm first swaps the elements of each row and column
    and then reverses each row.
    """
    m = len(matrix)

    # Swap elements of each row and column
    for i in range(m):
        for j in range(i, m):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # Reverse each row
    for i in range(m):
        matrix[i] = matrix[i][::-1]

    # Reverse each row of the matrix.
    for i in range(n):
        for j in range(n // 2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n - 1 - j]
            matrix[i][n - 1 - j] = temp
