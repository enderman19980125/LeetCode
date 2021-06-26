class Solution:
    @staticmethod
    def __check(num: str, first: str, second: str) -> bool:
        if len(first) >= 2 and first.startswith('0'):
            return False
        if len(second) >= 2 and second.startswith('0'):
            return False

        num = num[len(first) + len(second):]
        if not num:
            return False

        while num:
            current = str(int(first) + int(second))
            if not num.startswith(current):
                return False
            first, second = second, current
            num = num[len(current):]

        return True

    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(n):
            for j in range(i + 1, n):
                first = num[:i + 1]
                second = num[i + 1:j + 1]
                if self.__check(num, first, second):
                    return True
        return False


def test(input_content: str, std_answer: bool) -> None:
    solution = Solution()
    answer = solution.isAdditiveNumber(input_content)
    print(f"%s %s %s" % (answer == std_answer, answer, std_answer))


if __name__ == '__main__':
    test(input_content="112358", std_answer=True)
    test(input_content="199100199", std_answer=True)
    test(input_content="12", std_answer=False)
    test(input_content="102", std_answer=False)
    test(input_content="10212", std_answer=True)
    test(input_content="101101202", std_answer=True)
    test(input_content="101101222", std_answer=False)
