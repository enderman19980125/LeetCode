class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            stairs[i] = stairs[i - 2] + stairs[i - 1]
        return stairs[n]


if __name__ == '__main__':
    solution = Solution()

    answer = solution.climbStairs(2)
    print(answer, 2)

    answer = solution.climbStairs(3)
    print(answer, 3)

    answer = solution.climbStairs(1)
    print(answer, 1)

    answer = solution.climbStairs(4)
    print(answer, 5)
