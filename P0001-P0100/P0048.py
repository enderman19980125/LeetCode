from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(int(n // 2)):
            for j in range(i, n - i - 1):
                matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i] = \
                    matrix[n - 1 - j][i], matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j]


if __name__ == '__main__':
    solution = Solution()

    answer = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution.rotate(answer)
    print(answer)
    print([[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    answer = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    solution.rotate(answer)
    print(answer)
    print([[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])

    answer = [[]]
    solution.rotate(answer)
    print(answer)
    print([[]])

    answer = [[1]]
    solution.rotate(answer)
    print(answer)
    print([[1]])

    answer = [[1, 2], [3, 4]]
    solution.rotate(answer)
    print(answer)
    print([[3, 1], [4, 2]])
