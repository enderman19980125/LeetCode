from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = board[i]
            column = [board[k][i] for k in range(9)]
            row = list(filter(lambda x: x != ".", row))
            column = list(filter(lambda x: x != ".", column))
            if len(row) != len(set(row)):
                return False
            if len(column) != len(set(column)):
                return False

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                square = [board[i][j], board[i][j + 1], board[i][j + 2],
                          board[i + 1][j], board[i + 1][j + 1], board[i + 1][j + 2],
                          board[i + 2][j], board[i + 2][j + 1], board[i + 2][j + 2]
                          ]
                square = list(filter(lambda x: x != ".", square))
                if len(square) != len(set(square)):
                    return False

        return True


if __name__ == '__main__':
    solution = Solution()

    matrix = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    answer = solution.isValidSudoku(matrix)
    print(answer, True)

    matrix = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    answer = solution.isValidSudoku(matrix)
    print(answer, False)
