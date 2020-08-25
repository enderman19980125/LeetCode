from typing import List


class Solution:
    def __init__(self):
        self.target = 0
        self.candidates = []
        self.ans_list = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []

        self.target = target
        self.candidates = sorted(candidates)
        self.ans_list = []

        self._search(0, 0, [])
        return self.ans_list

    def _search(self, k: int, s: int, ans: List[int]) -> None:
        if s == self.target and (k == len(self.candidates) or ans[-1] != self.candidates[k]):
            self.ans_list.append(ans)
        if s >= self.target or k == len(self.candidates):
            return
        if ans == [] or self.candidates[k] != ans[-1]:
            self._search(k + 1, s, ans.copy())
        s += self.candidates[k]
        ans.append(self.candidates[k])
        self._search(k + 1, s, ans.copy())


if __name__ == '__main__':
    solution = Solution()

    answer = solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    print(answer, [[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]])

    answer = solution.combinationSum2([2, 5, 2, 1, 2], 5)
    print(answer, [[1, 2, 2], [5]])

    answer = solution.combinationSum2([], 0)
    print(answer, [])

    answer = solution.combinationSum2([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
    print(answer)
