class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1

        flag = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            flag = -1
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor

        k = 1
        while (d := divisor << 1) < dividend:
            divisor = d
            k <<= 1

        ans = 0
        while divisor != 0:
            if dividend - divisor >= 0:
                ans += k
                dividend -= divisor
            else:
                divisor >>= 1
                k >>= 1

        if flag == -1:
            ans = -ans

        return ans


if __name__ == '__main__':
    solution = Solution()

    answer = solution.divide(10, 3)
    print(answer, 3)

    answer = solution.divide(7, -3)
    print(answer, -2)

    answer = solution.divide(0, 1)
    print(answer, 0)

    answer = solution.divide(0, -1)
    print(answer, 0)

    answer = solution.divide(1, 2)
    print(answer, 0)

    answer = solution.divide(9, 3)
    print(answer, 3)

    answer = solution.divide(-2 ** 31, -1)
    print(answer, 2 ** 31 - 1)

    answer = solution.divide(2 ** 31 - 1, -1)
    print(answer, -2 ** 31 + 1)

    answer = solution.divide(2 ** 31 - 1, -2 ** 31)
    print(answer, 0)

    answer = solution.divide(-2 ** 31, 2 ** 31 - 1)
    print(answer, -1)
