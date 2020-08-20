from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = ""
        length = min([len(s) for s in strs])
        for i in range(length + 1):
            prefix = strs[0][:i]
            if all([s.startswith(prefix) for s in strs]):
                ans = prefix
            else:
                break
        return ans


if __name__ == '__main__':
    solution = Solution()
    answer = solution.longestCommonPrefix(["flower", "flow", "flight"])
    print(answer, "fl")
    answer = solution.longestCommonPrefix(["dog", "racecar", "car"])
    print(answer, "")
    answer = solution.longestCommonPrefix(["tutu", "tu", "tubenben"])
    print(answer, "tu")
    answer = solution.longestCommonPrefix([])
    print(answer, "")
