from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m - 1, -1, -1):
            nums1[i + n] = nums1[i]

        i, j, k = n, 0, 0
        while i < m + n and j < n:
            if nums1[i] <= nums2[j]:
                nums1[k] = nums1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1

        if j < n:
            for kk in range(k, m + n):
                nums1[kk] = nums2[j]
                j += 1


if __name__ == '__main__':
    solution = Solution()

    nums1_list, nums2_list = [1, 2, 3, 0, 0, 0], [2, 5, 6]
    solution.merge(nums1_list, 3, nums2_list, 3)
    print(nums1_list, [1, 2, 2, 3, 5, 6])

    nums1_list, nums2_list = [], []
    solution.merge(nums1_list, 0, nums2_list, 0)
    print(nums1_list, [])

    nums1_list, nums2_list = [0], [1]
    solution.merge(nums1_list, 0, nums2_list, 1)
    print(nums1_list, [1])

    nums1_list, nums2_list = [1], []
    solution.merge(nums1_list, 1, nums2_list, 0)
    print(nums1_list, [1])

    nums1_list, nums2_list = [0, 0], [1, 2]
    solution.merge(nums1_list, 0, nums2_list, 2)
    print(nums1_list, [1, 2])

    nums1_list, nums2_list = [1, 2], []
    solution.merge(nums1_list, 2, nums2_list, 0)
    print(nums1_list, [1, 2])

    nums1_list, nums2_list = [1, 2, 3, 5, 0, 0, 0], [2, 4, 6]
    solution.merge(nums1_list, 4, nums2_list, 3)
    print(nums1_list, [1, 2, 2, 3, 4, 5, 6])

    nums1_list, nums2_list = [1, 2, 5, 6, 0, 0, 0], [2, 3, 4]
    solution.merge(nums1_list, 4, nums2_list, 3)
    print(nums1_list, [1, 2, 2, 3, 4, 5, 6])

    nums1_list, nums2_list = [1, 2, 4, 0, 0, 0, 0], [2, 3, 5, 6]
    solution.merge(nums1_list, 3, nums2_list, 4)
    print(nums1_list, [1, 2, 2, 3, 4, 5, 6])

    nums1_list, nums2_list = [1, 5, 6, 0, 0, 0, 0], [2, 2, 3, 4]
    solution.merge(nums1_list, 3, nums2_list, 4)
    print(nums1_list, [1, 2, 2, 3, 4, 5, 6])
