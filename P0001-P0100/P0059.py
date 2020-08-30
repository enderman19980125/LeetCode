from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        i, j, k = 0, 0, 1
        dx, dy = 0, 1
        used = [[False for _ in range(n)] for _ in range(n)]
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        while 0 <= i < n and 0 <= j < n and not used[i][j]:
            matrix[i][j] = k
            k += 1
            used[i][j] = True
            ii, jj = i + dx, j + dy
            if ii < 0 or jj < 0 or ii >= n or jj >= n or used[ii][jj]:
                if (dx, dy) == (0, 1):
                    dx, dy = 1, 0
                elif (dx, dy) == (0, -1):
                    dx, dy = -1, 0
                elif (dx, dy) == (1, 0):
                    dx, dy = 0, -1
                elif (dx, dy) == (-1, 0):
                    dx, dy = 0, 1
            i, j = i + dx, j + dy
        return matrix


if __name__ == '__main__':
    solution = Solution()

    answer = solution.generateMatrix(3)
    print(answer, [[1, 2, 3], [8, 9, 4], [7, 6, 5]])

    answer = solution.generateMatrix(2)
    print(answer, [[1, 2], [4, 3]])

    answer = solution.generateMatrix(1)
    print(answer, [[1]])
