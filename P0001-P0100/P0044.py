class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p == "":
            return True
        if s != "" and p == "":
            return False

        while p.find("**") >= 0:
            p = p.replace("**", "*")

        ns, np = len(s), len(p)
        dp = [[False for _ in range(np + 1)] for _ in range(ns + 1)]
        dp[0][0] = True
        dp[0][1] = True if p[0] == "*" else False
        for i in range(1, ns + 1):
            for j in range(1, np + 1):
                if p[j - 1] == "*" and j == 1:
                    dp[i][j] = True
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1] or dp[i - 1][j - 1]
                elif p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[ns][np]


if __name__ == '__main__':
    solution = Solution()

    # official examples
    answer = solution.isMatch("aa", "a")
    print(answer, False)

    answer = solution.isMatch("aa", "*")
    print(answer, True)

    answer = solution.isMatch("cb", "?a")
    print(answer, False)

    answer = solution.isMatch("adceb", "*a*b")
    print(answer, True)

    answer = solution.isMatch("acdcb", "a*c?b")
    print(answer, False)

    answer = solution.isMatch("ho", "**ho")
    print(answer, True)

    # normal examples
    answer = solution.isMatch("a", "a")
    print(answer, True)

    answer = solution.isMatch("a", "b")
    print(answer, False)

    # *? examples
    answer = solution.isMatch("abcde", "*")
    print(answer, True)

    answer = solution.isMatch("abcde", "*?")
    print(answer, True)

    answer = solution.isMatch("abcde", "*????")
    print(answer, True)

    answer = solution.isMatch("abcde", "*?????")
    print(answer, True)

    answer = solution.isMatch("abcde", "*??????")
    print(answer, False)

    # ?* examples
    answer = solution.isMatch("abcde", "*")
    print(answer, True)

    answer = solution.isMatch("abcde", "?*")
    print(answer, True)

    answer = solution.isMatch("abcde", "????*")
    print(answer, True)

    answer = solution.isMatch("abcde", "?????*")
    print(answer, True)

    answer = solution.isMatch("abcde", "??????*")
    print(answer, False)

    # multiple-* examples

    answer = solution.isMatch("abcde", "***abcde")
    print(answer, True)

    answer = solution.isMatch("abcde", "abcde***")
    print(answer, True)

    # empty examples
    answer = solution.isMatch("", "*")
    print(answer, True)

    answer = solution.isMatch("", "")
    print(answer, True)

    answer = solution.isMatch("a", "")
    print(answer, False)
