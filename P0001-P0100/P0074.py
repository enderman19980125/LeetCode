from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0 or target < matrix[0][0] or target > matrix[m - 1][n - 1]:
            return False

        k = 0
        for i in range(m):
            if target < matrix[i][0]:
                break
            k = i

        i, j = 0, n - 1
        while i < j:
            m = (i + j) // 2
            if matrix[k][m] < target:
                i = m + 1
            else:
                j = m

        return matrix[k][i] == target


if __name__ == '__main__':
    solution = Solution()

    answer = solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3)
    print(answer, True)

    answer = solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 13)
    print(answer, False)

    answer = solution.searchMatrix([], 0)
    print(answer, False)

    answer = solution.searchMatrix([[]], 1)
    print(answer, False)

    answer = solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 0)
    print(answer, False)

    answer = solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 60)
    print(answer, False)

    answer = solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 8)
    print(answer, False)

    answer = solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 21)
    print(answer, False)

    answer = solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 1)
    print(answer, True)

    answer = solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 7)
    print(answer, True)

    answer = solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 23)
    print(answer, True)

    answer = solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 50)
    print(answer, True)
