from typing import List


class SolutionRecursion:
    def __init__(self):
        self.n = 0
        self.ans = 0

    def totalNQueens(self, n: int) -> int:
        if n == 0:
            return 0
        self.n = n
        self.ans = 0
        board = [["."] * n] * n
        self._search(0, board)
        return self.ans

    def _search(self, i: int, board: List[List[str]]) -> None:
        if i == self.n:
            self.ans += 1
            return
        for j in range(self.n):
            if board[i][j] == ".":
                new_board = [row.copy() for row in board]
                for k in range(self.n):
                    new_board[i][k] = new_board[k][j] = "-"
                    if i - k >= 0 and j - k >= 0:
                        new_board[i - k][j - k] = "-"
                    if i - k >= 0 and j + k < self.n:
                        new_board[i - k][j + k] = "-"
                    if i + k < self.n and j - k >= 0:
                        new_board[i + k][j - k] = "-"
                    if i + k < self.n and j + k < self.n:
                        new_board[i + k][j + k] = "-"
                new_board[i][j] = "Q"
                self._search(i + 1, new_board)


class Solution:
    def __init__(self):
        self.max = 0
        self.ans = 0

    def totalNQueens(self, n: int) -> int:
        if n == 0:
            return 0
        self.max = 2 ** n - 1
        self.ans = 0
        self._search(0, 0, 0)
        return self.ans

    def _search(self, row: int, ld: int, rd: int) -> None:
        if row == self.max:
            self.ans += 1
            return
        pos = ~(row | ld | rd) & self.max
        while pos > 0:
            p = pos & (~pos + 1)
            pos -= p
            self._search(row | p, ((ld | p) << 1) & self.max, ((rd | p) >> 1) & self.max)


if __name__ == '__main__':
    solution = Solution()

    answer = solution.totalNQueens(4)
    print(answer, 2)

    answer = solution.totalNQueens(0)
    print(answer, 0)

    answer = solution.totalNQueens(1)
    print(answer, 1)

    answer = solution.totalNQueens(2)
    print(answer, 0)
