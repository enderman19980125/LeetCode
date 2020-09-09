from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        m, n = len(matrix), len(matrix[0])
        ones_matrix = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == "1" and j == n - 1:
                    ones_matrix[i][j] = 1
                elif matrix[i][j] == "1" and j < n - 1:
                    ones_matrix[i][j] = ones_matrix[i][j + 1] + 1

        max_area = 0
        for j in range(n):
            i0 = 0
            while i0 < m:
                while i0 < m and ones_matrix[i0][j] == 0:
                    i0 += 1
                if i0 == m:
                    break
                i1 = i0
                while i1 < m and ones_matrix[i1][j] > 0:
                    i1 += 1
                i1 -= 1

                heights = [ones_matrix[i][j] for i in range(i0, i1 + 1)]
                d = len(heights)
                left, right = [-1] * d, [d] * d
                mono_stack = []
                for k, height in enumerate(heights):
                    while mono_stack and heights[mono_stack[-1]] >= height:
                        right[mono_stack[-1]] = k
                        mono_stack.pop()
                    left[k] = mono_stack[-1] if mono_stack else -1
                    mono_stack.append(k)

                for k, height in enumerate(heights):
                    area = height * (right[k] - left[k] - 1)
                    max_area = max(max_area, area)

                i0 = i1 + 2

        return max_area


if __name__ == '__main__':
    solution = Solution()

    answer = solution.maximalRectangle([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ])
    print(answer, 6)

    answer = solution.maximalRectangle([[]])
    print(answer, 0)

    answer = solution.maximalRectangle([["0"]])
    print(answer, 0)

    answer = solution.maximalRectangle([["1"]])
    print(answer, 1)

    answer = solution.maximalRectangle([
        ["1", "0", "1", "1", "0"],
        ["1", "0", "0", "0", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "0"]
    ])
    print(answer, 8)

    answer = solution.maximalRectangle([
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"]
    ])
    print(answer, 20)
