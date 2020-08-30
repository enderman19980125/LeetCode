class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip(" ").split(" ")[-1])


if __name__ == '__main__':
    solution = Solution()

    answer = solution.lengthOfLastWord("Hello World")
    print(answer, 5)

    answer = solution.lengthOfLastWord("a ")
    print(answer, 1)

    answer = solution.lengthOfLastWord("")
    print(answer, 0)

    answer = solution.lengthOfLastWord("a")
    print(answer, 1)

    answer = solution.lengthOfLastWord("abc")
    print(answer, 3)

    answer = solution.lengthOfLastWord("I love Cony")
    print(answer, 4)
