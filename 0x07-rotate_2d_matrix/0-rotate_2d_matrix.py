#!/usr/bin/env python3
"""Rotates an n x n 2D matrix 90 degrees clockwise in-place."""


def rotate_2d_matrix(matrix: list) -> None:
    """Rotates a 2D square matrix 90 degrees clockwise in-place.

    Modifies the input matrix directly.

    Args:
        matrix (list): A 2D square matrix.
    """

    n = len(matrix)
    # Transpose the upper left triangle of the matrix.
    for i in range(n):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    # Reverse each row of the matrix.
    for i in range(n):
        for j in range(n // 2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n - 1 - j]
            matrix[i][n - 1 - j] = temp