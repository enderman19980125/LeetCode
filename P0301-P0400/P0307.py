from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.__a = [0] * (1 + len(nums))
        for i, num in enumerate(nums):
            self.update(i, num)

    @staticmethod
    def __lowbit(index: int) -> int:
        return index & (-index)

    def __update(self, index: int, val: int) -> None:
        index += 1
        while index < len(self.__a):
            self.__a[index] += val
            index += self.__lowbit(index)

    def __sum(self, index: int) -> int:
        s = 0
        index += 1
        while index > 0:
            s += self.__a[index]
            index -= self.__lowbit(index)
        return s

    def update(self, index: int, val: int) -> None:
        current = self.sumRange(index, index)
        self.__update(index, val - current)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.__sum(right)
        else:
            return self.__sum(right) - self.__sum(left - 1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

def test_1() -> None:
    num_array = NumArray([1, 3, 5])

    answer = num_array.sumRange(0, 2)
    std_answer = 9
    print(f"%s %s %s" % (answer == std_answer, answer, std_answer))

    num_array.update(1, 2)

    answer = num_array.sumRange(0, 2)
    std_answer = 8
    print(f"%s %s %s" % (answer == std_answer, answer, std_answer))


def test_2() -> None:
    num_array = NumArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    answer = num_array.sumRange(0, 0)
    std_answer = 0
    print(f"%s %s %s" % (answer == std_answer, answer, std_answer))

    answer = num_array.sumRange(0, 1)
    std_answer = 1
    print(f"%s %s %s" % (answer == std_answer, answer, std_answer))

    answer = num_array.sumRange(0, 9)
    std_answer = 45
    print(f"%s %s %s" % (answer == std_answer, answer, std_answer))

    num_array.update(1, 5)

    answer = num_array.sumRange(0, 1)
    std_answer = 5
    print(f"%s %s %s" % (answer == std_answer, answer, std_answer))

    answer = num_array.sumRange(0, 9)
    std_answer = 49
    print(f"%s %s %s" % (answer == std_answer, answer, std_answer))


if __name__ == '__main__':
    test_1()
    test_2()
