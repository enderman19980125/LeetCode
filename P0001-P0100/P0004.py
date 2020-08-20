from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
        else:
            return nums[(len(nums) - 1) // 2]


if __name__ == '__main__':
    solution = Solution()
    answer = solution.findMedianSortedArrays([1, 3], [2])
    print(answer, 2)
    answer = solution.findMedianSortedArrays([1, 2], [3, 4])
    print(answer, 2.5)
    answer = solution.findMedianSortedArrays([0, 0], [0, 0])
    print(answer, 0)
    answer = solution.findMedianSortedArrays([], [1])
    print(answer, 1)
    answer = solution.findMedianSortedArrays([2], [])
    print(answer, 2)
