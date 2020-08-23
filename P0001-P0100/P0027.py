from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0
        for num in nums:
            if num != val:
                nums[p] = num
                p += 1
        return p


if __name__ == '__main__':
    solution = Solution()

    nums_list = [3, 2, 2, 3]
    answer = solution.removeElement(nums_list, 3)
    print(answer, 2, nums_list[:answer], [2, 2])

    nums_list = [0, 1, 2, 2, 3, 0, 4, 2]
    answer = solution.removeElement(nums_list, 2)
    print(answer, 5, nums_list[:answer], [0, 1, 3, 0, 4])

    nums_list = [2, 2, 2]
    answer = solution.removeElement(nums_list, 2)
    print(answer, 0, nums_list[:answer], [])
