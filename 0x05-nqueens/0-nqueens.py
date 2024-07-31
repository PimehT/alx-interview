#!/usr/bin/python3
"""Solves the N-Queens puzzle."""

import sys


def is_valid(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def place_queens(board, row, n, result):
    """Use backtracking to place queens on the board."""
    if row == n:
        result.append([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            place_queens(board, row + 1, n, result)
            # backtrack: remove the queen and try next column
            board[row] = -1


def solve_n_queens(n):
    """Solve the N-Queens problem and return the list of solutions."""
    result = []
    board = [-1] * n
    place_queens(board, 0, n, result)
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(N)
    for solution in solutions:
        print(solution)
