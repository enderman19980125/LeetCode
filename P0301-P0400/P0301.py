from typing import Tuple, List


class Solution:
    def __init__(self):
        self.__answer = set()

    @staticmethod
    def __calc_num_to_remove(s: str) -> Tuple[int, int]:
        num_left = 0
        num_right = 0

        for c in s:
            if c == '(':
                num_left += 1
            elif c == ')' and num_left == 0:
                num_right += 1
            elif c == ')' and num_left > 0:
                num_left -= 1

        return num_left, num_right

    def __remove(self, s: str, k: int, num_unpaired_left: int, num_left_to_remove: int, num_right_to_remove: int) -> None:
        if num_left_to_remove == num_right_to_remove == 0 and self.__calc_num_to_remove(s) == (0, 0):
            self.__answer.add(s)
            return

        if k == len(s):
            return

        if s[k] == '(':
            self.__remove(s, k + 1, num_unpaired_left + 1, num_left_to_remove, num_right_to_remove)
            if num_left_to_remove > 0:
                self.__remove(s[:k] + s[k + 1:], k, num_unpaired_left, num_left_to_remove - 1, num_right_to_remove)

        elif s[k] == ')':
            self.__remove(s, k + 1, num_unpaired_left - 1, num_left_to_remove, num_right_to_remove)
            if num_right_to_remove > 0:
                self.__remove(s[:k] + s[k + 1:], k, num_unpaired_left, num_left_to_remove, num_right_to_remove - 1)

        else:
            self.__remove(s, k + 1, num_unpaired_left, num_left_to_remove, num_right_to_remove)

    def removeInvalidParentheses(self, s: str) -> List[str]:
        num_left_to_remove, num_right_to_remove = self.__calc_num_to_remove(s)
        self.__remove(s, 0, 0, num_left_to_remove, num_right_to_remove)
        return list(self.__answer)


def test(input_content: str, std_answer: List[str]) -> None:
    solution = Solution()
    answer = solution.removeInvalidParentheses(input_content)
    answer.sort()
    std_answer.sort()
    print(f"%s %s %s" % (answer == std_answer, answer, std_answer))


if __name__ == '__main__':
    test(input_content="()())()", std_answer=["(())()", "()()()"])
    test(input_content="(a)())()", std_answer=["(a())()", "(a)()()"])
    test(input_content=")(", std_answer=[""])
    test(input_content=")()))", std_answer=["()"])
    test(input_content=")((()", std_answer=["()"])
    test(input_content="()())", std_answer=["()()", "(())"])
    test(input_content="(", std_answer=[""])
    test(input_content="((", std_answer=[""])
    test(input_content=")", std_answer=[""])
    test(input_content="))", std_answer=[""])
    test(input_content="()", std_answer=["()"])
    test(input_content="", std_answer=[""])
    test(input_content="a", std_answer=["a"])
    test(input_content="x(", std_answer=["x"])
