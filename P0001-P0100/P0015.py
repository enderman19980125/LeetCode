from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, a in enumerate(nums):
            if i >= 1 and a == nums[i - 1]:
                continue
            if a > 0:
                break
            k = len(nums) - 1
            for j, b in enumerate(nums[i + 1:], start=i + 1):
                if j >= i + 2 and b == nums[j - 1]:
                    continue
                if a + b > 0:
                    break
                c = -(a + b)
                while j < k and nums[k] > c:
                    k -= 1
                if j < k and c == nums[k]:
                    ans.append([a, b, c])
        return ans


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()

        new_nums = []
        value, count = None, 0
        for num in nums:
            if value == num:
                count += 1
            else:
                count = 1
                value = num
            if num != 0 and count <= 2:
                new_nums.append(num)
            if num == 0 and count == 1:
                new_nums.append(num)
            if num == 0 and count == 3:
                ans.add((0, 0, 0))
        nums = new_nums

        for i, a in enumerate(nums):
            if a > 0:
                break
            k = len(nums) - 1
            for j, b in enumerate(nums[i + 1:], start=i + 1):
                if a + b > 0:
                    break
                c = -(a + b)
                while j < k and nums[k] > c:
                    k -= 1
                if j < k and c == nums[k]:
                    triplet = tuple(sorted([a, b, c]))
                    ans.add(triplet)
        ans = list([[a, b, c] for a, b, c in ans])
        return ans


if __name__ == '__main__':
    solution = Solution()
    answer = solution.threeSum([-1, 0, 1, 2, -1, -4])
    print(answer, [[-1, 0, 1], [-1, -1, 2]])
    answer = solution.threeSum([0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1])
    print(answer, [[0, 0, 0], [-1, 0, 1]])

    solution2 = Solution2()
    answer = solution2.threeSum([-1, 0, 1, 2, -1, -4])
    print(answer, [[-1, 0, 1], [-1, -1, 2]])
    answer = solution2.threeSum([0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1])
    print(answer, [[0, 0, 0], [-1, 0, 1]])
