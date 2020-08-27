from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        self.ans = []
        self._search(0, [], nums)
        return self.ans

    def _search(self, k: int, p: List[int], u: List[int]) -> None:
        if not u:
            self.ans.append(p)
            return
        for num in set(u):
            uu = u.copy()
            uu.remove(num)
            self._search(k + 1, p + [num], uu)


if __name__ == '__main__':
    solution = Solution()

    answer = solution.permuteUnique([1, 1, 2])
    print(answer)
    print([[1, 1, 2], [1, 2, 1], [2, 1, 1]])

    answer = solution.permuteUnique([])
    print(answer)
    print([])

    answer = solution.permuteUnique([1])
    print(answer)
    print([[1]])

    answer = solution.permuteUnique([1, 1])
    print(answer)
    print([[1, 1]])
