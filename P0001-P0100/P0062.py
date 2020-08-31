class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1 if i * j == 0 else 0 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[m - 1][n - 1]


if __name__ == '__main__':
    solution = Solution()

    answer = solution.uniquePaths(3, 2)
    print(answer, 3)

    answer = solution.uniquePaths(7, 3)
    print(answer, 28)

    answer = solution.uniquePaths(1, 1)
    print(answer, 1)

    answer = solution.uniquePaths(1, 2)
    print(answer, 1)

    answer = solution.uniquePaths(2, 1)
    print(answer, 1)

    answer = solution.uniquePaths(1, 100)
    print(answer, 1)

    answer = solution.uniquePaths(100, 1)
    print(answer, 1)

    answer = solution.uniquePaths(100, 100)
    print(answer)
