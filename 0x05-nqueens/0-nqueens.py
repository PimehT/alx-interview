#!/usr/bin/python3
""" The program should print every possible solution to the problem """
import sys


def solve_n_queens(n):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or board[i] - i == col - row \
                or board[i] + i == col + row:
                return False
        return True
    
    def place_queens(board, row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                place_queens(board, row + 1)
    
    result = []
    place_queens([-1] * n, 0)
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N\n')
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number\n')
        exit(1)
    if n > 3:
        solutions = solve_n_queens(n)
        for sol in solutions:
            for i in range(n):
                sol[i] = [i, sol[i]]
            print(sol)
    else:
        print('N must be at least 4\n')
