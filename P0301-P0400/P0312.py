from typing import List


class Solution:
    def __init__(self):
        self.nums = []
        self.coins = []

    def search(self, left: int, right: int) -> int:
        if self.coins[left][right] >= 0:
            return self.coins[left][right]
        elif left > right:
            return 0

        max_coins = 0
        for k in range(left, right + 1):
            max_coins = max(max_coins, self.search(left, k - 1) + self.search(k + 1, right) +
                            self.nums[left - 1] * self.nums[k] * self.nums[right + 1])
        self.coins[left][right] = max_coins
        return max_coins

    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        self.nums = [1] + nums + [1]
        self.coins = [[-1 for _ in range(n + 2)] for _ in range(n + 2)]
        return self.search(1, n)


def test(input_content: List[int], std_answer: int) -> None:
    solution = Solution()
    answer = solution.maxCoins(input_content)
    print(f"%s %s %s" % (answer == std_answer, answer, std_answer))


if __name__ == '__main__':
    test(input_content=[3, 1, 5, 8], std_answer=167)
    test(input_content=[1, 5], std_answer=10)
    test(input_content=[5], std_answer=5)
    test(input_content=[2, 3, 4, 5, 6], std_answer=246)
