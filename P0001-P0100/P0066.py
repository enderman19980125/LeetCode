from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k = len(digits) - 1
        digits[k] += 1
        while k >= 1 and digits[k] >= 10:
            digits[k - 1] += 1
            digits[k] %= 10
            k -= 1
        if digits[0] >= 10:
            digits.insert(0, 1)
            digits[1] %= 10
        return digits


if __name__ == '__main__':
    solution = Solution()

    answer = solution.plusOne([1, 2, 3])
    print(answer, [1, 2, 4])

    answer = solution.plusOne([4, 3, 2, 1])
    print(answer, [4, 3, 2, 2])

    answer = solution.plusOne([0])
    print(answer, [1])

    answer = solution.plusOne([9, 9, 9])
    print(answer, [1, 0, 0, 0])

    answer = solution.plusOne([9])
    print(answer, [1, 0])

    answer = solution.plusOne([8, 9])
    print(answer, [9, 0])

    answer = solution.plusOne([9, 9])
    print(answer, [1, 0, 0])
