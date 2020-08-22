from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        p, q = 0, 0
        while True:
            while q < len(nums) and nums[p] == nums[q]:
                q += 1
            if q == len(nums):
                break
            p += 1
            nums[p] = nums[q]

        return p + 1


if __name__ == '__main__':
    solution = Solution()

    nums_list = [1, 1, 2]
    answer = solution.removeDuplicates(nums_list)
    print(answer, 2, nums_list[:answer], [1, 2])

    nums_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    answer = solution.removeDuplicates(nums_list)
    print(answer, 5, nums_list[:answer], [0, 1, 2, 3, 4])

    nums_list = [0, 0]
    answer = solution.removeDuplicates(nums_list)
    print(answer, 1, nums_list[:answer], [0])

    nums_list = []
    answer = solution.removeDuplicates(nums_list)
    print(answer, 0, nums_list[:answer], [])
