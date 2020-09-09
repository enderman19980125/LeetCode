class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return self._match(s1, s2)

    @staticmethod
    def _to_list(s: str) -> list:
        return sorted([c for c in s])

    def _match(self, s: str, target: str) -> bool:
        n = len(s)
        if n == 1:
            return s == target
        for i in range(1, n):
            left_s, right_s = s[:i], s[i:]
            left_s_list, right_s_list = self._to_list(left_s), self._to_list(right_s)

            left_target, right_target = target[:i], target[i:]
            left_target_list, right_target_list = self._to_list(left_target), self._to_list(right_target)
            if left_s_list == left_target_list and right_s_list == right_target_list:
                if self._match(left_s, left_target) and self._match(right_s, right_target):
                    return True

            left_target, right_target = target[-i:], target[:-i]
            left_target_list, right_target_list = self._to_list(left_target), self._to_list(right_target)
            if left_s_list == left_target_list and right_s_list == right_target_list:
                if self._match(left_s, left_target) and self._match(right_s, right_target):
                    return True

        return False


if __name__ == '__main__':
    solution = Solution()

    answer = solution.isScramble("great", "rgeat")
    print(answer, True)

    answer = solution.isScramble("abcde", "caebd")
    print(answer, False)

    answer = solution.isScramble("a", "a")
    print(answer, True)

    answer = solution.isScramble("abcdbdacbdac", "bdacabcdbdac")
    print(answer, True)

    answer = solution.isScramble("a", "b")
    print(answer, False)

    answer = solution.isScramble("abcde", "edcab")
    print(answer, True)
