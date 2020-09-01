from typing import List


class Solution:
    def __init__(self):
        self.is_find = False
        self.m = 0
        self.n = 0
        self.board = [[]]
        self.word = ""

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.is_find = False
        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        self.word = word
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == self.word[0]:
                    self._get(i, j, 1, [(i, j)])
                if self.is_find:
                    return True
        return False

    def _get(self, x: int, y: int, k: int, used_position: List[tuple]) -> None:
        if k == len(self.word):
            self.is_find = True
            return
        dx_list, dy_list = [0, 0, 1, -1], [-1, 1, 0, 0]
        for dx, dy in zip(dx_list, dy_list):
            xx, yy = x + dx, y + dy
            if 0 <= xx < self.m and 0 <= yy < self.n and self.board[xx][yy] == self.word[k] \
                    and (xx, yy) not in used_position:
                self._get(xx, yy, k + 1, used_position + [(xx, yy)])
            if self.is_find:
                return


if __name__ == '__main__':
    solution = Solution()

    answer = solution.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "ABCCED")
    print(answer, True)

    answer = solution.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "SEE")
    print(answer, True)

    answer = solution.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "ABCB")
    print(answer, False)

    answer = solution.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "ASADFCCESEE")
    print(answer, True)

    answer = solution.exist([['A']], "A")
    print(answer, True)

    answer = solution.exist([['A']], "AB")
    print(answer, False)

    answer = solution.exist([['A', 'B', 'C']], "AB")
    print(answer, True)

    answer = solution.exist([['A', 'B', 'C']], "ABC")
    print(answer, True)
