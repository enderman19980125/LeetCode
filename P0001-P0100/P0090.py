from typing import List


class Solution:
    def __init__(self):
        self.nums = []
        self.subsets = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums = sorted(nums)
        self.subsets = []
        self._search(0, [])
        return self.subsets

    def _search(self, k: int, subset: List[int]) -> None:
        if k == len(self.nums):
            self.subsets.append(subset)
            return
        if subset and subset[-1] == self.nums[k]:
            self._search(k + 1, subset + [self.nums[k]])
        else:
            self._search(k + 1, subset)
            self._search(k + 1, subset + [self.nums[k]])


if __name__ == '__main__':
    solution = Solution()

    answer = solution.subsetsWithDup([1, 2, 2])
    print(answer, [[2], [1], [1, 2, 2], [2, 2], [1, 2], []])

    answer = solution.subsetsWithDup([4, 4, 4, 1, 4])
    print(answer, [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]])

    answer = solution.subsetsWithDup([])
    print(answer, [[]])

    answer = solution.subsetsWithDup([1])
    print(answer, [[], [1]])

    answer = solution.subsetsWithDup([1, 1])
    print(answer, [[], [1], [1, 1]])
