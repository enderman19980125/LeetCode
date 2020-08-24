from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        i, j = 0, n - 1
        while i < j:
            mid = (i + j) // 2 + 1
            if nums[mid] <= target:
                i = mid
            else:
                j = mid - 1

        if nums[i] >= target:
            return i
        else:
            return i + 1


if __name__ == '__main__':
    solution = Solution()

    answer = solution.searchInsert([1, 3, 5, 6], 5)
    print(answer, 2)

    answer = solution.searchInsert([1, 3, 5, 6], 2)
    print(answer, 1)

    answer = solution.searchInsert([1, 3, 5, 6], 7)
    print(answer, 4)

    answer = solution.searchInsert([1, 3, 5, 6], 0)
    print(answer, 0)

    answer = solution.searchInsert([], 0)
    print(answer, 0)

    answer = solution.searchInsert([1], 1)
    print(answer, 0)

    answer = solution.searchInsert([1], -1)
    print(answer, 0)

    answer = solution.searchInsert([1], 2)
    print(answer, 1)

    answer = solution.searchInsert([1, 3], 0)
    print(answer, 0)

    answer = solution.searchInsert([1, 3], 2)
    print(answer, 1)

    answer = solution.searchInsert([1, 3], 4)
    print(answer, 2)
