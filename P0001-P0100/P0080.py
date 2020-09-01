from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = -1
        for num in nums:
            if k <= 0 or not nums[k - 1] == nums[k] == num:
                k += 1
                nums[k] = num
        return k + 1


if __name__ == '__main__':
    solution = Solution()

    nums_list = [1, 1, 1, 2, 2, 3]
    std = [1, 1, 2, 2, 3]
    answer = solution.removeDuplicates(nums_list)
    print(nums_list[:answer], std)

    nums_list = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    std = [0, 0, 1, 1, 2, 3, 3]
    answer = solution.removeDuplicates(nums_list)
    print(nums_list[:answer], std)

    nums_list = []
    std = []
    answer = solution.removeDuplicates(nums_list)
    print(nums_list[:answer], std)

    nums_list = [0]
    std = [0]
    answer = solution.removeDuplicates(nums_list)
    print(nums_list[:answer], std)

    nums_list = [0, 0, 0, 0, 0]
    std = [0, 0]
    answer = solution.removeDuplicates(nums_list)
    print(nums_list[:answer], std)

    nums_list = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    std = [0, 0, 1, 1, 2, 2]
    answer = solution.removeDuplicates(nums_list)
    print(nums_list[:answer], std)

    nums_list = [0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    std = [0, 1, 1, 2, 2]
    answer = solution.removeDuplicates(nums_list)
    print(nums_list[:answer], std)
