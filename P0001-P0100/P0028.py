class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i, _ in enumerate(haystack):
            for j, p in enumerate(needle):
                if i + j >= len(haystack) or haystack[i + j] != p:
                    break
            else:
                break
        else:
            i = -1
        return i


if __name__ == '__main__':
    solution = Solution()

    answer = solution.strStr("hello", "ll")
    print(answer, 2)

    answer = solution.strStr("aaaaa", "bba")
    print(answer, -1)

    answer = solution.strStr("aaaaa", "")
    print(answer, 0)

    answer = solution.strStr("", "")
    print(answer, 0)

    answer = solution.strStr("aaa", "aaaa")
    print(answer, -1)

    answer = solution.strStr("mississippi", "issipi")
    print(answer, -1)
