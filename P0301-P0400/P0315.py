from typing import List


class Solution:
    def __init__(self):
        self.tree = [0] * 20002

    @staticmethod
    def __lowbit(index: int) -> int:
        return index & -index

    def __add(self, index: int) -> None:
        while index < len(self.tree):
            self.tree[index] += 1
            index += Solution.__lowbit(index)

    def __get_sum(self, index: int) -> int:
        s = 0
        while index > 0:
            s += self.tree[index]
            index -= Solution.__lowbit(index)
        return s

    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        for i in range(n - 1, -1, -1):
            ans[i] = self.__get_sum(nums[i] - 1 + 10001)
            self.__add(nums[i] + 10001)

        return ans


def test(input_content: List[int], std_answer: List[int]) -> None:
    solution = Solution()
    answer = solution.countSmaller(input_content)
    print(f"%s %s %s" % (answer == std_answer, answer, std_answer))


if __name__ == '__main__':
    test(input_content=[5, 2, 6, 1], std_answer=[2, 1, 1, 0])
    test(input_content=[-1], std_answer=[0])
    test(input_content=[-1, -1], std_answer=[0, 0])
    test(input_content=[-1, -2, -3, -4, -5], std_answer=[4, 3, 2, 1, 0])
    test(input_content=[-1, -2, -4, -4, -5], std_answer=[4, 3, 1, 1, 0])
    test(input_content=[-10000, -1000, -100, -10, -1, 1, 10, 100, 1000, 10000], std_answer=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    test(input_content=[i for i in range(-10000, 10001, 1)], std_answer=[0] * 20001)
