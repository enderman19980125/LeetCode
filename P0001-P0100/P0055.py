from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if i == n - 1 or last < i:
                break
            last = max(last, i + num)
        return last >= n - 1


if __name__ == '__main__':
    solution = Solution()

    answer = solution.canJump([2, 3, 1, 1, 4])
    print(answer, True)

    answer = solution.canJump([3, 2, 1, 0, 4])
    print(answer, False)

    answer = solution.canJump([0])
    print(answer, True)

    answer = solution.canJump([1])
    print(answer, True)

    answer = solution.canJump([2, 0, 0, 0, 4])
    print(answer, False)
