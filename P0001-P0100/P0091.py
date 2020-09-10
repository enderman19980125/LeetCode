class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] + [0] * n

        for i in range(1, n + 1):
            if i >= 2 and "10" <= s[i - 2:i] <= "26":
                dp[i] += dp[i - 2]
            if "1" <= s[i - 1] <= "9":
                dp[i] += dp[i - 1]

        return dp[n]


if __name__ == '__main__':
    solution = Solution()

    answer = solution.numDecodings("12")
    print(answer, 2)

    answer = solution.numDecodings("226")
    print(answer, 3)

    answer = solution.numDecodings("0")
    print(answer, 0)

    answer = solution.numDecodings("01")
    print(answer, 0)

    answer = solution.numDecodings("012")
    print(answer, 0)

    answer = solution.numDecodings("2626")
    print(answer, 4)
