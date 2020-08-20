class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        p = -1
        length = 0
        for i, c in enumerate(s):
            if c in d.keys():
                length = max(length, i - max(d[c], p))
                p = max(p, d[c])
            else:
                length = max(length, i - p)
            d[c] = i
        length = max(length, len(s) - 1 - p)
        return length


if __name__ == '__main__':
    solution = Solution()
    answer = solution.lengthOfLongestSubstring("abcabcbb")
    print(answer, 3)
    answer = solution.lengthOfLongestSubstring("bbbbb")
    print(answer, 1)
    answer = solution.lengthOfLongestSubstring("pwwkew")
    print(answer, 3)
    answer = solution.lengthOfLongestSubstring("abba")
    print(answer, 2)
    answer = solution.lengthOfLongestSubstring("abcde")
    print(answer, 5)
    answer = solution.lengthOfLongestSubstring("dvdf")
    print(answer, 3)
