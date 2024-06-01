#!/usr/bin/python3
import sys

def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)

def solve_nqueens(N):
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve(board, col):
        if col >= N:
            solution = []
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return True
        res = False
        for i in range(N):
            if is_safe(board, i, col):
                board[i][col] = 1
                res = solve(board, col + 1) or res
                board[i][col] = 0
        return res

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve(board, 0)
    return solutions

if len(sys.argv) != 2:
    print_usage_and_exit()

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

solutions = solve_nqueens(N)
for solution in solutions:
    print(solution)
