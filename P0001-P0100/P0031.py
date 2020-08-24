from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == sorted(nums, reverse=True):
            nums.reverse()
            return

        n = len(nums)
        k = n - 1
        for k in range(n - 1, 0, -1):
            if k >= 1 and nums[k - 1] < nums[k]:
                min_pos = k
                for i in range(k, n):
                    if nums[k - 1] < nums[i] < nums[min_pos]:
                        min_pos = i
                nums[k - 1], nums[min_pos] = nums[min_pos], nums[k - 1]
                break

        for i in range(k, n):
            min_pos = i + nums[i:].index(min(nums[i:]))
            nums[i], nums[min_pos] = nums[min_pos], nums[i]


if __name__ == '__main__':
    solution = Solution()

    nums_list = [1, 2, 3]
    solution.nextPermutation(nums_list)
    print(nums_list, [1, 3, 2])

    nums_list = [3, 2, 1]
    solution.nextPermutation(nums_list)
    print(nums_list, [1, 2, 3])

    nums_list = [1, 1, 5]
    solution.nextPermutation(nums_list)
    print(nums_list, [1, 5, 1])

    nums_list = [1, 3, 2]
    solution.nextPermutation(nums_list)
    print(nums_list, [2, 1, 3])

    nums_list = [2, 3, 1]
    solution.nextPermutation(nums_list)
    print(nums_list, [3, 1, 2])

    nums_list = [2, 2, 7, 5, 4, 3, 2, 2, 1]
    solution.nextPermutation(nums_list)
    print(nums_list, [2, 3, 1, 2, 2, 2, 4, 5, 7])

    nums_list = [1, 4, 3, 2]
    solution.nextPermutation(nums_list)
    print(nums_list, [2, 1, 3, 4])

    nums_list = [2, 1, 4, 3]
    solution.nextPermutation(nums_list)
    print(nums_list, [2, 3, 1, 4])

    nums_list = []
    solution.nextPermutation(nums_list)
    print(nums_list, [])

    nums_list = [1]
    solution.nextPermutation(nums_list)
    print(nums_list, [1])

    nums_list = [1, 1, 1]
    solution.nextPermutation(nums_list)
    print(nums_list, [1, 1, 1])
