from typing import List


class Solution:
    def __init__(self):
        self.nums = []
        self.ans = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.ans = []
        self._get(0, [])
        return self.ans

    def _get(self, k: int, s: List[int]) -> None:
        if k == len(self.nums):
            self.ans.append(s)
            return
        self._get(k + 1, s)
        self._get(k + 1, s + [self.nums[k]])


if __name__ == '__main__':
    solution = Solution()

    answer = solution.subsets([1, 2, 3])
    print(answer, [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []])

    answer = solution.subsets([])
    print(answer, [[]])

    answer = solution.subsets([1, 2])
    print(answer, [[], [1], [2], [1, 2]])
