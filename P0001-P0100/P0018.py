from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        new_nums = []
        value, count = None, 0
        for num in nums:
            if num == value:
                count += 1
            else:
                value = num
                count = 1
            if count <= 4:
                new_nums.append(num)
        nums = new_nums

        ans = []
        for i, a in enumerate(nums):
            if i >= 1 and a == nums[i - 1]:
                continue
            if 4 * a > target:
                break
            for j, b in enumerate(nums[i + 1:], start=i + 1):
                if j >= i + 2 and b == nums[j - 1]:
                    continue
                if a + 3 * b > target:
                    break
                m = len(nums) - 1
                for k, c in enumerate(nums[j + 1:], start=j + 1):
                    if k >= j + 2 and c == nums[k - 1]:
                        continue
                    if a + b + 2 * c > target:
                        break
                    d = nums[m]
                    while k < m and a + b + c + d > target:
                        m -= 1
                        d = nums[m]
                    if k < m and a + b + c + d == target:
                        ans.append([a, b, c, d])
        return ans


if __name__ == '__main__':
    solution = Solution()
    answer = solution.fourSum([1, 0, -1, 0, -2, 2], 0)
    print(answer, [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]])
