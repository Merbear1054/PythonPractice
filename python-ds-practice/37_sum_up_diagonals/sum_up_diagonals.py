def sum_up_diagonals(matrix):
    """Return sum of TL-BR and BL-TR diagonals in a square matrix."""
    n = len(matrix)
    return sum(matrix[i][i] + matrix[i][n - 1 - i] for i in range(n))
