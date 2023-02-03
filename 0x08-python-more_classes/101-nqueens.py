#!/usr/bin/python3
import sys


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
            print()


def isSafe(board, row, col):
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


def solveNQUtil(board, col):
    if col >= N:
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQUtil(board, col+1) is True:
                return True
            board[i][col] = 0
            return False


def solveNQ():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    if solveNQUtil(board, 0) is False:
        print("Solution does not exist")
        return False
    printSolution(board)
    if __name__ == '__main__':
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
        solveNQ()
        sys.exit(0)
