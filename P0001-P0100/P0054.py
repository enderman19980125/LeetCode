from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        ans = []
        i, j = 0, 0
        dx, dy = 0, 1
        n, m = len(matrix), len(matrix[0])
        used = [[False for _ in range(m)] for _ in range(n)]
        while 0 <= i < n and 0 <= j < m and not used[i][j]:
            ans.append(matrix[i][j])
            used[i][j] = True
            ii, jj = i + dx, j + dy
            if ii < 0 or jj < 0 or ii >= n or jj >= m or used[ii][jj]:
                if (dx, dy) == (0, 1):
                    dx, dy = 1, 0
                elif (dx, dy) == (0, -1):
                    dx, dy = -1, 0
                elif (dx, dy) == (1, 0):
                    dx, dy = 0, -1
                elif (dx, dy) == (-1, 0):
                    dx, dy = 0, 1
            i, j = i + dx, j + dy
        return ans


if __name__ == '__main__':
    solution = Solution()

    answer = solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(answer, [1, 2, 3, 6, 9, 8, 7, 4, 5])

    answer = solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(answer, [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])

    answer = solution.spiralOrder([[2, 5], [8, 4], [0, -1]])
    print(answer, [2, 5, 4, -1, 0, 8])

    answer = solution.spiralOrder([[]])
    print(answer, [])

    answer = solution.spiralOrder([[1]])
    print(answer, [1])

    answer = solution.spiralOrder([[1, 2]])
    print(answer, [1, 2])

    answer = solution.spiralOrder([[1], [2]])
    print(answer, [1, 2])

    answer = solution.spiralOrder([[1, 2], [3, 4]])
    print(answer, [1, 2, 3, 4])
