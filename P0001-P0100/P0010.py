class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p.startswith("*"):
            return False
        s, p = "A" + s, "A" + p
        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
        for i, cs in enumerate(s, start=1):
            for j, cp in enumerate(p, start=1):
                previous_cp = p[j - 2] if j >= 2 else None
                if cp == "*" and previous_cp == ".":
                    dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                elif cp == "*":
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and cs == previous_cp)
                elif cp == "." or cs == cp:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]


if __name__ == '__main__':
    solution = Solution()
    answer = solution.isMatch("aa", "a")
    print(answer, False)
    answer = solution.isMatch("aa", "a*")
    print(answer, True)
    answer = solution.isMatch("ab", ".*")
    print(answer, True)
    answer = solution.isMatch("aab", "c*a*b")
    print(answer, True)
    answer = solution.isMatch("mississippi", "mis*is*p*.")
    print(answer, False)
    answer = solution.isMatch("aaaaa", "a.*")
    print(answer, True)
    answer = solution.isMatch("aaaaa", "a.*a")
    print(answer, True)
    answer = solution.isMatch("aaaaa", "a.*aaaa")
    print(answer, True)
    answer = solution.isMatch("aaaaa", "a.*aaaaa")
    print(answer, False)
    answer = solution.isMatch("aaaaa", "a*")
    print(answer, True)
    answer = solution.isMatch("aaaaa", "a*aaaaa")
    print(answer, True)
    answer = solution.isMatch("aaaaa", "a*aaaaaa")
    print(answer, False)
    answer = solution.isMatch("", "a*")
    print(answer, True)
    answer = solution.isMatch("", ".*")
    print(answer, True)
