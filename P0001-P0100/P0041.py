from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 1
        while True:
            is_edit = False
            for i, num in enumerate(nums):
                if 0 < num <= n and num != i + 1 and nums[num - 1] != num:
                    nums[num - 1], nums[i] = nums[i], nums[num - 1]
                    is_edit = True
            if not is_edit:
                break
        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        return n + 1


if __name__ == '__main__':
    solution = Solution()

    answer = solution.firstMissingPositive([1, 2, 0])
    print(answer, 3)

    answer = solution.firstMissingPositive([3, 4, -1, 1])
    print(answer, 2)

    answer = solution.firstMissingPositive([7, 8, 9, 11, 12])
    print(answer, 1)

    answer = solution.firstMissingPositive([])
    print(answer, 1)

    answer = solution.firstMissingPositive([1])
    print(answer, 2)

    answer = solution.firstMissingPositive([2])
    print(answer, 1)

    answer = solution.firstMissingPositive([1, 2, 3])
    print(answer, 4)

    answer = solution.firstMissingPositive([1, 2, 4])
    print(answer, 3)

    answer = solution.firstMissingPositive([2, 3, 4])
    print(answer, 1)

    answer = solution.firstMissingPositive([1, 1])
    print(answer, 2)
