class Solution:
    def myPow(self, x: float, n: int) -> float:
        sgn = 1.0 if n >= 0 else -1.0
        n = abs(n)
        ans = self._pow(x, n)
        if sgn == -1:
            ans = 1.0 / ans
        return ans

    def _pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        y = self._pow(x, n // 2)
        return y * y * x if n % 2 == 1 else y * y


class SolutionRecurrence:
    def myPow(self, x: float, n: int) -> float:
        sgn = 1.0 if n >= 0 else -1.0
        n = abs(n)
        ans = self._pow(x, n)
        if sgn == -1:
            ans = 1.0 / ans
        return ans

    def _pow(self, x: float, n: int) -> float:
        ans = 1.0
        while n > 0:
            if n % 2 == 1:
                ans *= x
            x *= x
            n //= 2
        return ans


if __name__ == '__main__':
    solution = Solution()

    answer = solution.myPow(2, 10)
    print(answer, 1024)

    answer = solution.myPow(2.1, 3)
    print(answer, 9.261)

    answer = solution.myPow(2, -2)
    print(answer, 0.25)

    answer = solution.myPow(2, -2147483648)
    print(answer, 0)

    answer = solution.myPow(2, 0)
    print(answer, 1)

    answer = solution.myPow(-2, 4)
    print(answer, 16)
