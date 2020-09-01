class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        i = 0
        min_window = ""
        s_dict = {c: 0 for c in s}
        t_dict = {c: 0 for c in t}
        for c in t:
            s_dict[c] = 0
            t_dict[c] += 1

        for j, c in enumerate(s):
            s_dict[c] += 1
            while i < j and (s[i] not in t_dict.keys() or s_dict[s[i]] > t_dict[s[i]]):
                s_dict[s[i]] -= 1
                i += 1
            is_correct = True
            for ch in t_dict.keys():
                if s_dict[ch] < t_dict[ch]:
                    is_correct = False
                    break
            if is_correct and (min_window == "" or j - i + 1 < len(min_window)):
                min_window = s[i:j + 1]
        return min_window


if __name__ == '__main__':
    solution = Solution()

    answer = solution.minWindow("ADOBECODEBANC", "ABC")
    print(answer, "BANC")

    answer = solution.minWindow("ABDEFGHIJKLMN", "ABC")
    print(answer, "")

    answer = solution.minWindow("ABDEFGHIJKLMNC", "ABC")
    print(answer, "ABDEFGHIJKLMNC")

    answer = solution.minWindow("A", "A")
    print(answer, "A")

    answer = solution.minWindow("AAA", "A")
    print(answer, "A")

    answer = solution.minWindow("A", "")
    print(answer, "")

    answer = solution.minWindow("ABOOOBCBA", "ABB")
    print(answer, "BCBA")
