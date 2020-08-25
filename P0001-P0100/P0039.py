from typing import List


class Solution:
    def __init__(self):
        self.target = 0
        self.candidates = []
        self.ans_list = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []

        self.target = target
        self.candidates = candidates
        self.ans_list = []

        self._search(0, 0, [])
        return self.ans_list

    def _search(self, k: int, s: int, ans: List[int]) -> None:
        if s == self.target:
            self.ans_list.append(ans)
            return
        if k == len(self.candidates):
            return
        self._search(k + 1, s, ans.copy())
        while s <= self.target:
            s += self.candidates[k]
            ans.append(self.candidates[k])
            self._search(k + 1, s, ans.copy())


if __name__ == '__main__':
    solution = Solution()

    answer = solution.combinationSum([2, 3, 6, 7], 7)
    print(answer, [[7], [2, 2, 3]])

    answer = solution.combinationSum([2, 3, 5], 8)
    print(answer, [[2, 2, 2, 2], [2, 3, 3], [3, 5]])

    answer = solution.combinationSum([], 0)
    print(answer, [])

    answer = solution.combinationSum([1], 1)
    print(answer, [[1]])

    answer = solution.combinationSum([1], 3)
    print(answer, [[1, 1, 1]])

    answer = solution.combinationSum([1, 2, 3], 3)
    print(answer, [[1, 1, 1], [1, 2], [3]])
