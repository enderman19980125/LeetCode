class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(1, n):
            ss = ""
            value, count = None, 0
            for c in s:
                if value == c:
                    count += 1
                else:
                    ss += (str(count) + value) if value else ""
                    value, count = c, 1
            ss += str(count) + value
            s = ss
        return s


if __name__ == '__main__':
    solution = Solution()

    answer = solution.countAndSay(1)
    print(answer, "1")

    answer = solution.countAndSay(2)
    print(answer, "11")

    answer = solution.countAndSay(3)
    print(answer, "21")

    answer = solution.countAndSay(4)
    print(answer, "1211")

    answer = solution.countAndSay(30)
    print(answer)
