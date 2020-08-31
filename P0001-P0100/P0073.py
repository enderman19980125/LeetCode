from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_columns = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            is_row_zeros = False
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_columns.append(j)
                    is_row_zeros = True
            if is_row_zeros:
                for j in range(n):
                    matrix[i][j] = 0
        for i in range(m):
            for j in zero_columns:
                matrix[i][j] = 0


if __name__ == '__main__':
    solution = Solution()

    mat = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    std = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    solution.setZeroes(mat)
    print(mat)
    print(std)

    mat = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    std = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    solution.setZeroes(mat)
    print(mat)
    print(std)

    mat = [[0, 1], [3, 4]]
    std = [[0, 0], [0, 4]]
    solution.setZeroes(mat)
    print(mat)
    print(std)
