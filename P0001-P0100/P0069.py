class Solution:
    def mySqrt(self, x: int) -> int:
        p, q = 0, x
        while p < q:
            m = (p + q) // 2 + 1
            if m ** 2 > x:
                q = m - 1
            else:
                p = m
        return p


if __name__ == '__main__':
    solution = Solution()

    answer = solution.mySqrt(4)
    print(answer, 2)

    answer = solution.mySqrt(8)
    print(answer, 2)

    answer = solution.mySqrt(6)
    print(answer, 2)

    answer = solution.mySqrt(0)
    print(answer, 0)

    answer = solution.mySqrt(1)
    print(answer, 1)

    answer = solution.mySqrt(3)
    print(answer, 1)

    answer = solution.mySqrt(63)
    print(answer, 7)

    answer = solution.mySqrt(64)
    print(answer, 8)
