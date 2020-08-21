from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        new_nums = []
        value, count = None, 0
        for num in nums:
            if num == value:
                count += 1
            else:
                value = num
                count = 1
            if count <= 3:
                new_nums.append(num)
        nums = new_nums

        ans = sum(nums[:3])
        min_limit = target - abs(target - ans)
        max_limit = target + abs(target - ans)

        for i, a in enumerate(nums):
            if i >= 1 and a == nums[i - 1]:
                continue
            if 3 * a > max_limit:
                break
            k_max = len(nums) - 1
            for j, b in enumerate(nums[i + 1:], start=i + 1):
                if j >= i + 2 and b == nums[j - 1]:
                    continue
                if a + 2 * b > max_limit:
                    break
                while j < k_max and a + b + nums[k_max] > max_limit:
                    k_max -= 1
                k = k_max
                c = nums[k]
                while j < k and a + b + c > min_limit:
                    if abs(a + b + c - target) < abs(ans - target):
                        ans = a + b + c
                        min_limit = target - abs(target - ans)
                        max_limit = target + abs(target - ans)
                    k -= 1
                    c = nums[k]
        return ans


if __name__ == '__main__':
    solution = Solution()
    answer = solution.threeSumClosest([-1, 2, 1, -4], 1)
    print(answer, 2)
    answer = solution.threeSumClosest([0, 0, 0, 1, 1, 1], -1)
    print(answer, 0)
    answer = solution.threeSumClosest([0, 0, 0, 1, 1, 1], 4)
    print(answer, 3)
    answer = solution.threeSumClosest([0, 1, 2], 4)
    print(answer, 3)
