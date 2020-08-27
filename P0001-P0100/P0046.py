from typing import List


class Solution:
    def __init__(self):
        self.nums = []
        self.ans = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        self.nums = nums
        self.ans = []
        self._search(0, [])
        return self.ans

    def _search(self, k: int, p: List[int]) -> None:
        if k == len(self.nums):
            self.ans.append(p)
            return
        for num in self.nums:
            if num not in p:
                self._search(k + 1, p + [num])


if __name__ == '__main__':
    solution = Solution()

    answer = solution.permute([1, 2, 3])
    print(answer)
    print([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])

    answer = solution.permute([])
    print(answer)
    print([])

    answer = solution.permute([1])
    print(answer)
    print([[1]])

    answer = solution.permute([1, 2])
    print(answer)
    print([[1, 2], [2, 1]])
