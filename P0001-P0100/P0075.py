from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n0, n1, n2 = 0, 0, 0
        for num in nums:
            if num == 0:
                n0 += 1
            elif num == 1:
                n1 += 1
            elif num == 2:
                n2 += 1
        for i in range(n0):
            nums[i] = 0
        for i in range(n0, n0 + n1):
            nums[i] = 1
        for i in range(n0 + n1, n0 + n1 + n2):
            nums[i] = 2


if __name__ == '__main__':
    solution = Solution()

    nums_list = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums_list)
    print(nums_list, [0, 0, 1, 1, 2, 2])

    nums_list = []
    solution.sortColors(nums_list)
    print(nums_list, [])

    nums_list = [0]
    solution.sortColors(nums_list)
    print(nums_list, [0])

    nums_list = [1]
    solution.sortColors(nums_list)
    print(nums_list, [1])

    nums_list = [2]
    solution.sortColors(nums_list)
    print(nums_list, [2])

    nums_list = [2, 1, 0]
    solution.sortColors(nums_list)
    print(nums_list, [0, 1, 2])
