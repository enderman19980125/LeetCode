class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            dp[i][0] = i
        for j in range(1, n2 + 1):
            dp[0][j] = j
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + int(word1[i - 1] != word2[j - 1]))
        return dp[n1][n2]


if __name__ == '__main__':
    solution = Solution()

    answer = solution.minDistance("horse", "ros")
    print(answer, 3)

    answer = solution.minDistance("intention", "execution")
    print(answer, 5)

    answer = solution.minDistance("a", "b")
    print(answer, 1)

    answer = solution.minDistance("", "b")
    print(answer, 1)

    answer = solution.minDistance("a", "")
    print(answer, 1)

    answer = solution.minDistance("", "")
    print(answer, 0)

    answer = solution.minDistance("abc", "def")
    print(answer, 3)

    answer = solution.minDistance("abc", "aabd")
    print(answer, 2)
