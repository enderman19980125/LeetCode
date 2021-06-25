from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.__prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            self.__prefix_sum.append(self.__prefix_sum[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.__prefix_sum[right]
        else:
            return self.__prefix_sum[right] - self.__prefix_sum[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

def test() -> None:
    num_array = NumArray([-2, 0, 3, -5, 2, -1])

    answer = num_array.sumRange(0, 2)
    std_answer = 1
    print("%s %s %s" % (answer == std_answer, answer, std_answer))

    answer = num_array.sumRange(2, 5)
    std_answer = -1
    print("%s %s %s" % (answer == std_answer, answer, std_answer))

    answer = num_array.sumRange(0, 5)
    std_answer = -3
    print("%s %s %s" % (answer == std_answer, answer, std_answer))


if __name__ == '__main__':
    test()
