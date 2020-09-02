from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        n = len(nums)
        while n > 1 and nums[n - 1] == nums[0]:
            n -= 1

        i, j = 0, n - 1
        while i < j:
            mid = (i + j) // 2 + 1
            if nums[mid] >= nums[0]:
                i = mid
            else:
                j = mid - 1
        k = i

        if target >= nums[0]:
            i, j = 0, k
        else:
            i, j = min(k + 1, n - 1), n - 1

        while i < j:
            mid = (i + j) // 2 + 1
            if nums[mid] <= target:
                i = mid
            else:
                j = mid - 1

        return nums[i] == target


if __name__ == '__main__':
    solution = Solution()

    answer = solution.search([2, 5, 6, 0, 0, 1, 2], 0)
    print(answer, True)

    answer = solution.search([2, 5, 6, 0, 0, 1, 2], 3)
    print(answer, False)

    answer = solution.search([1], 0)
    print(answer, False)

    answer = solution.search([], 0)
    print(answer, False)

    answer = solution.search([0], 0)
    print(answer, True)

    answer = solution.search([0], 1)
    print(answer, False)

    answer = solution.search([0, 0], 1)
    print(answer, False)

    answer = solution.search([3, 3, 3, 4, 5, 1, 2, 3, 3, 3], 3)
    print(answer, True)

    answer = solution.search([3, 1, 2, 3, 3, 3], 3)
    print(answer, True)

    answer = solution.search([3, 3, 3, 4, 5, 3], 3)
    print(answer, True)
