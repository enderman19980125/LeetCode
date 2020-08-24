from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
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
            i, j = min(n - 1, k + 1), n - 1

        while i < j:
            mid = (i + j) // 2
            if target > nums[mid]:
                i = mid + 1
            else:
                j = mid

        ans = i if nums[i] == target else -1
        return ans


if __name__ == '__main__':
    solution = Solution()

    answer = solution.search([4, 5, 6, 7, 0, 1, 2], 0)
    print(answer, 4)

    answer = solution.search([4, 5, 6, 7, 0, 1, 2], 3)
    print(answer, -1)

    answer = solution.search([1], 0)
    print(answer, -1)

    answer = solution.search([1, 1], 0)
    print(answer, -1)

    answer = solution.search([1, 1], 1)
    print(answer, 0)

    answer = solution.search([1, 1, 1], 0)
    print(answer, -1)

    answer = solution.search([1, 1, 1], 1)
    print(answer, 0)

    answer = solution.search([1, 2, 3], 2)
    print(answer, 1)

    answer = solution.search([3, 1, 2], 3)
    print(answer, 0)

    answer = solution.search([3, 1, 2], 1)
    print(answer, 1)

    answer = solution.search([3, 1, 2], 2)
    print(answer, 2)

    answer = solution.search([3, 4, 5, 1, 2, 3], 3)
    print(answer, 0)

    answer = solution.search([3, 4, 5, 1, 2, 3], 1)
    print(answer, 3)
