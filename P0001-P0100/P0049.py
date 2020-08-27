from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            chars_list = sorted([c for c in s])
            chars = "".join(chars_list)
            if chars in d.keys():
                d[chars].append(s)
            else:
                d[chars] = [s]
        ans = list(d.values())
        return ans


if __name__ == '__main__':
    solution = Solution()

    answer = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(answer, [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]])

    answer = solution.groupAnagrams(["aab", "aba", "baa", "aaa"])
    print(answer, [["aab", "aba", "baa"], ["aaa"]])

    answer = solution.groupAnagrams(["a"])
    print(answer, [["a"]])

    answer = solution.groupAnagrams([])
    print(answer, [])
