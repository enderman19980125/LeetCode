from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0, 0] for _ in range(n)]
        dp[0] = [-prices[0], 0, 0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])

        return max(dp[n - 1])


def test(input_content: List[int], std_answer: int) -> None:
    solution = Solution()
    answer = solution.maxProfit(input_content)
    print(f"%s %s %s" % (answer == std_answer, answer, std_answer))


if __name__ == '__main__':
    test(input_content=[1, 2, 3, 0, 2], std_answer=3)
    test(input_content=[1], std_answer=0)
    test(input_content=[1, 1], std_answer=0)
    test(input_content=[1, 2], std_answer=1)
    test(input_content=[2, 1], std_answer=0)
    test(input_content=[1, 2, 3, 4], std_answer=3)
    test(input_content=[1, 3, 4, 2], std_answer=3)
    test(input_content=[1, 2, 3, 1, 2, 3, 1, 2, 3], std_answer=4)
    test(input_content=[1, 3, 4, 1, 3, 4, 1, 3, 4], std_answer=7)
    test(input_content=[1, 3, 4, 1, 3, 4, 1, 3, 4, 1, 3, 4], std_answer=9)
