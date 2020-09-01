from typing import List


class Solution:
    def __init__(self):
        self.n = 0
        self.k = 0
        self.ans = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n = n
        self.k = k
        self.ans = []
        self._get([])
        return self.ans

    def _get(self, c: List[int]):
        if len(c) == self.k:
            self.ans.append(c)
            return
        start = max(c) + 1 if c else 1
        for i in range(start, self.n + 1):
            if i not in c:
                self._get(c + [i])


if __name__ == '__main__':
    solution = Solution()

    answer = solution.combine(4, 2)
    print(answer, [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]])

    answer = solution.combine(1, 1)
    print(answer, [[1]])

    answer = solution.combine(2, 1)
    print(answer, [[1], [2]])

    answer = solution.combine(3, 2)
    print(answer, [[1, 2], [1, 3], [2, 3]])
