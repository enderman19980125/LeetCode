from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_sum, max_count = nums[0], 1
        s, c = 0, 0
        for num in nums:
            if s >= 0:
                s, c = s + num, c + 1
            else:
                s, c = num, 1
            if s > max_sum:
                max_sum, max_count = s, max(max_count, c)

        return max_sum


if __name__ == '__main__':
    solution = Solution()

    answer = solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(answer, 6)

    answer = solution.maxSubArray([])
    print(answer, 0)

    answer = solution.maxSubArray([-1])
    print(answer, -1)

    answer = solution.maxSubArray([0])
    print(answer, 0)

    answer = solution.maxSubArray([1])
    print(answer, 1)

    answer = solution.maxSubArray([1, -2])
    print(answer, 1)

    answer = solution.maxSubArray([-2, 1])
    print(answer, 1)

    answer = solution.maxSubArray([2, -1])
    print(answer, 2)

    answer = solution.maxSubArray([-1, 2])
    print(answer, 2)
