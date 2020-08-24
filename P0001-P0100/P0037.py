from typing import List


class Solution:
    def __init__(self):
        self.is_solved = False
        self.board = None
        self.unknown_cells = []
        self.used_columns = [["."] for _ in range(9)]
        self.used_rows = [["."] for _ in range(9)]
        self.used_squares = [["."] for _ in range(9)]

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.is_solved = False
        self.board = board
        self.unknown_cells = []
        self.used_columns = [["."] for _ in range(9)]
        self.used_rows = [["."] for _ in range(9)]
        self.used_squares = [["."] for _ in range(9)]

        for i in range(9):
            row = board[i]
            column = [board[k][i] for k in range(9)]
            row = list(filter(lambda x: x != ".", row))
            column = list(filter(lambda x: x != ".", column))
            self.used_rows[i] = row
            self.used_columns[i] = column

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                square = [board[i][j], board[i][j + 1], board[i][j + 2],
                          board[i + 1][j], board[i + 1][j + 1], board[i + 1][j + 2],
                          board[i + 2][j], board[i + 2][j + 1], board[i + 2][j + 2]
                          ]
                square = list(filter(lambda x: x != ".", square))
                self.used_squares[i // 3 * 3 + j // 3] = square

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    used_digits = set(self.used_rows[i] + self.used_columns[j] + self.used_squares[i // 3 * 3 + j // 3])
                    num_possible = 9 - len(used_digits)
                    self.unknown_cells.append((i, j, num_possible))
        self.unknown_cells.sort(key=lambda x: x[2])

        self._solve(0)

    def _solve(self, k: int):
        if k == len(self.unknown_cells):
            self.is_solved = True
            return
        i, j, _ = self.unknown_cells[k]
        used_digits = set(self.used_rows[i] + self.used_columns[j] + self.used_squares[i // 3 * 3 + j // 3])
        unused_digits = set(map(str, range(1, 10))).difference(used_digits)
        for digit in unused_digits:
            self.board[i][j] = digit
            self.used_rows[i].append(digit)
            self.used_columns[j].append(digit)
            self.used_squares[i // 3 * 3 + j // 3].append(digit)

            self._solve(k + 1)
            if self.is_solved:
                return

            self.board[i][j] = "."
            self.used_rows[i].remove(digit)
            self.used_columns[j].remove(digit)
            self.used_squares[i // 3 * 3 + j // 3].remove(digit)


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
    solved_matrix = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
    ]
    solution.solveSudoku(matrix)
    print(matrix)
    print(solved_matrix)
    print(matrix == solved_matrix)
