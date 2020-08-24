from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]

        i, j = 0, n - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid

        if nums[i] != target:
            return [-1, -1]

        left = i
        j = n - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                i = mid + 1
            else:
                j = mid
        right = i if nums[i] == target else i - 1

        return [left, right]


if __name__ == '__main__':
    solution = Solution()

    answer = solution.searchRange([5, 7, 7, 8, 8, 10], 8)
    print(answer, [3, 4])

    answer = solution.searchRange([5, 7, 7, 8, 8, 10], 6)
    print(answer, [-1, -1])

    answer = solution.searchRange([2, 2], 2)
    print(answer, [0, 1])

    answer = solution.searchRange([], 0)
    print(answer, [-1, -1])

    answer = solution.searchRange([0], 0)
    print(answer, [0, 0])

    answer = solution.searchRange([0], 1)
    print(answer, [-1, -1])

    answer = solution.searchRange([0, 0], 0)
    print(answer, [0, 1])

    answer = solution.searchRange([0, 0], 1)
    print(answer, [-1, -1])

    answer = solution.searchRange([0, 1], 0)
    print(answer, [0, 0])

    answer = solution.searchRange([0, 1], 1)
    print(answer, [1, 1])
