from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        steps = [n for _ in range(n)]
        steps[0] = 0
        for i, num in enumerate(nums):
            if steps[min(i + num, n - 1)] <= steps[i] + 1:
                continue
            for j in range(i + 1, min(i + num, n - 1) + 1):
                steps[j] = min(steps[j], steps[i] + 1)
        return steps[n - 1]


if __name__ == '__main__':
    solution = Solution()

    answer = solution.jump([2, 3, 1, 1, 4])
    print(answer, 2)

    answer = solution.jump([0])
    print(answer, 0)

    answer = solution.jump([5])
    print(answer, 0)

    answer = solution.jump([1, 1, 1, 1, 1, 1])
    print(answer, 5)

    answer = solution.jump([2, 0, 3, 0, 0, 2])
    print(answer, 2)

    answer = solution.jump([2, 0, 3, 0, 0, 2])
    print(answer, 2)
