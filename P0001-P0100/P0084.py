from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        n = len(heights)
        stack = []
        left = [-1] * n
        right = [n] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                right[stack[-1]] = i
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        max_area = 0
        for i in range(n):
            area = heights[i] * (right[i] - left[i] - 1)
            max_area = max(max_area, area)

        return max_area


if __name__ == '__main__':
    solution = Solution()

    answer = solution.largestRectangleArea([2, 1, 5, 6, 2, 3])
    print(answer, 10)

    answer = solution.largestRectangleArea([0, 0, 0, 0, 0, 0, 0, 0, 2147483647])
    print(answer, 2147483647)

    answer = solution.largestRectangleArea([1])
    print(answer, 1)

    answer = solution.largestRectangleArea([])
    print(answer, 0)

    answer = solution.largestRectangleArea([1, 2, 3, 1, 1])
    print(answer, 5)

    answer = solution.largestRectangleArea([1, 2, 3, 1, 6])
    print(answer, 6)

    answer = solution.largestRectangleArea([3, 2, 1, 0, 1])
    print(answer, 4)

    answer = solution.largestRectangleArea([3, 2, 1, 6, 1])
    print(answer, 6)
