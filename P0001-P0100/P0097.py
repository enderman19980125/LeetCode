class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False

        dp = [[False for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        dp[0][0] = True
        for i in range(n1 + 1):
            if s1[:i] == s3[:i]:
                dp[i][0] = True
            else:
                break
        for i in range(n2 + 1):
            if s2[:i] == s3[:i]:
                dp[0][i] = True
            else:
                break

        for m3 in range(1, n3 + 1):
            for m1 in range(1, m3):
                m2 = m3 - m1
                if m1 > n1 or m2 > n2:
                    continue
                dp[m1][m2] |= s1[m1 - 1] == s3[m3 - 1] and dp[m1 - 1][m2]
                dp[m1][m2] |= s2[m2 - 1] == s3[m3 - 1] and dp[m1][m2 - 1]

        return dp[n1][n2]


if __name__ == '__main__':
    solution = Solution()

    answer = solution.isInterleave("aabcc", "dbbca", "aadbbcbcac")
    print(answer, True)

    answer = solution.isInterleave("aabcc", "dbbca", "aadbbbaccc")
    print(answer, False)

    answer = solution.isInterleave("", "", "")
    print(answer, True)

    answer = solution.isInterleave("aabcc", "dbbca", "aadbcbbcac")
    print(answer, True)

    answer = solution.isInterleave(
        "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
        "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
        "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababb"
        "bababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    )
    print(answer, False)

    answer = solution.isInterleave("", "a", "a")
    print(answer, True)

    answer = solution.isInterleave("a", "", "a")
    print(answer, True)

    answer = solution.isInterleave("a", "b", "a")
    print(answer, False)

    answer = solution.isInterleave("ab", "", "a")
    print(answer, False)

    answer = solution.isInterleave("aaa", "bbb", "ababab")
    print(answer, True)

    answer = solution.isInterleave("aaa", "abb", "ababab")
    print(answer, False)

# "aa bc    c"
# "  d  bbca"
# "aadbcbbcac"
