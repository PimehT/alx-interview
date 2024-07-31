# 0x05. N Queens

## Description

A classic problem in computer science and mathematics, the N queens puzzle is the problem of placing N chess queens on an N×N chessboard so that no two queens threaten each other. Thus, a solution requires that no two queens share the same row, column, or diagonal.

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line

## Tasks

### 0. N queens

Write a program that solves the N queens problem.

- Usage: `nqueens N`
    - If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status 1
- where N must be an integer greater or equal to 4
    - If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status 1
    - If N is smaller than 4, print `N must be at least 4`, followed by a new line, and exit with the status 1
