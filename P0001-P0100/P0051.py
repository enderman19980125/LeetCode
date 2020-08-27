from typing import List


class Solution:
    def __init__(self):
        self.n = 0
        self.ans = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        self.n = n
        self.ans = []
        board = [["."] * n] * n
        self._search(0, board)
        return self.ans

    def _search(self, i: int, board: List[List[str]]) -> None:
        if i == self.n:
            board = ["".join(row).replace("-", ".") for row in board]
            self.ans.append(board)
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


if __name__ == '__main__':
    solution = Solution()

    answer = solution.solveNQueens(4)
    print(answer)
    print([[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])

    answer = solution.solveNQueens(0)
    print(answer)
    print([])

    answer = solution.solveNQueens(1)
    print(answer)
    print([["Q"]])

    answer = solution.solveNQueens(2)
    print(answer)
    print([])
