from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                for ii in range(i, m):
                    obstacleGrid[ii][0] = 0
                break
            obstacleGrid[i][0] = 1
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                for jj in range(j, n):
                    obstacleGrid[0][jj] = 0
                break
            obstacleGrid[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[m - 1][n - 1]


if __name__ == '__main__':
    solution = Solution()

    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    answer = solution.uniquePathsWithObstacles(grid)
    print(answer, 2)

    grid = [[0], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [1], [0], [0], [0], [0], [1], [0], [0],
            [0], [0], [0], [0], [0], [0], [0], [0], [1], [1], [0], [1], [0], [0], [1], [0], [0], [0], [0], [1]]
    answer = solution.uniquePathsWithObstacles(grid)
    print(answer, 0)

    grid = [[0]]
    answer = solution.uniquePathsWithObstacles(grid)
    print(answer, 1)

    grid = [[0, 0, 0]]
    answer = solution.uniquePathsWithObstacles(grid)
    print(answer, 1)

    grid = [[1, 0, 0]]
    answer = solution.uniquePathsWithObstacles(grid)
    print(answer, 0)

    grid = [[0, 1, 0]]
    answer = solution.uniquePathsWithObstacles(grid)
    print(answer, 0)

    grid = [[0, 0, 1]]
    answer = solution.uniquePathsWithObstacles(grid)
    print(answer, 0)

    grid = [[0], [0], [0]]
    answer = solution.uniquePathsWithObstacles(grid)
    print(answer, 1)

    grid = [[1], [0], [0]]
    answer = solution.uniquePathsWithObstacles(grid)
    print(answer, 0)

    grid = [[0], [1], [0]]
    answer = solution.uniquePathsWithObstacles(grid)
    print(answer, 0)

    grid = [[0], [0], [1]]
    answer = solution.uniquePathsWithObstacles(grid)
    print(answer, 0)

    grid = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    answer = solution.uniquePathsWithObstacles(grid)
    print(answer, 28)

    grid = [[0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0]]
    answer = solution.uniquePathsWithObstacles(grid)
    print(answer, 3)
