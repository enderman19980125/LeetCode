class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(0, len(s)):
            j = 0
            while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                j += 1
            j -= 1
            if 2 * j + 1 > len(ans):
                ans = s[i - j:i + j + 1]
        for i in range(0, len(s)):
            j = 0
            while i - j >= 0 and i + j + 1 < len(s) and s[i - j] == s[i + j + 1]:
                j += 1
            j -= 1
            if 2 * j + 2 > len(ans):
                ans = s[i - j:i + j + 2]
        return ans


if __name__ == '__main__':
    solution = Solution()
    answer = solution.longestPalindrome("babad")
    print(answer, "bab")
    answer = solution.longestPalindrome("cbbd")
    print(answer, "bb")
    answer = solution.longestPalindrome("abccbc")
    print(answer, "bccb")
