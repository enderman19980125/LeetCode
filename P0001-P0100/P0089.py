from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        codes = [0]
        for k in range(n):
            for i in range(2 ** k - 1, -1, -1):
                codes.append(codes[i] + (1 << k))
        return codes


if __name__ == '__main__':
    solution = Solution()

    answer = solution.grayCode(2)
    print(answer, [0, 1, 3, 2])

    answer = solution.grayCode(0)
    print(answer, [0])

    answer = solution.grayCode(1)
    print(answer, [0, 1])

    answer = solution.grayCode(5)
    print(answer)
