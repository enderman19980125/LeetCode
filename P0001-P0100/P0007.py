class Solution:
    def reverse(self, x: int) -> int:
        symbol = 1 if x >= 0 else -1
        x = abs(x)
        ans = 0
        while x != 0:
            ans = 10 * ans + x % 10
            x //= 10
        ans *= symbol
        if ans < -2 ** 31 or ans > 2 ** 31 - 1:
            ans = 0
        return ans


if __name__ == '__main__':
    solution = Solution()
    answer = solution.reverse(123)
    print(answer, 321)
    answer = solution.reverse(-123)
    print(answer, -321)
    answer = solution.reverse(120)
    print(answer, 21)
    answer = solution.reverse(-120)
    print(answer, -21)
    answer = solution.reverse(1)
    print(answer, 1)
    answer = solution.reverse(-1)
    print(answer, -1)
    answer = solution.reverse(0)
    print(answer, 0)
    answer = solution.reverse(2 ** 31 + 1)
    print(answer, 0)
    answer = solution.reverse(-2 ** 31)
    print(answer, 0)
