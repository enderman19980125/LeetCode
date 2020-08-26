from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pos = [i for i in range(n)]

        left, right = 0, n - 1
        while left + 1 <= right and height[left] <= height[left + 1]:
            pos[left] = -1
            left += 1
        while right - 1 >= left and height[right - 1] >= height[right]:
            pos[right] = -1
            right -= 1

        k = left + 1
        while k < right:
            for k in range(k, right):
                if height[k - 1] >= height[k] <= height[k + 1]:
                    break
            i, j = k, k
            while left <= i - 1 and pos[i - 1] == i - 1 and height[i - 1] >= height[i]:
                i -= 1
            while right >= j + 1 and pos[j + 1] == j + 1 and height[j] <= height[j + 1]:
                j += 1
            pos[i] = j
            for p in range(i + 1, j):
                pos[p] = 0
            k = j + 1

        while True:
            is_update = False
            k = left
            while k < right:
                a_left, a_right = k, pos[k]
                if a_right == right:
                    break
                b_right = pos[a_right]
                if height[a_left] >= height[a_right] <= height[b_right]:
                    pos[a_left], pos[a_right] = b_right, 0
                    is_update = True
                else:
                    k = a_right
            if not is_update:
                break

        ans = 0
        k = left
        while k < right:
            a_left, a_right = k, pos[k]
            h = min(height[a_left], height[a_right])
            for i in range(a_left + 1, a_right):
                ans += max(0, h - height[i])
            k = a_right

        return ans


class SolutionSum:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = height.copy()
        max_right = height.copy()

        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], max_left[i])
        for i in range(n - 2, 0, -1):
            max_right[i] = max(max_right[i], max_right[i + 1])

        ans = 0
        for i, h in enumerate(height):
            ans += min(max_left[i], max_right[i]) - h

        return ans


class SolutionStack:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        for i, h in enumerate(height):
            while stack and height[stack[-1]] <= h:
                k = stack[-1]
                stack.pop()
                if stack:
                    top = min(h, height[stack[-1]])
                    ans += (top - height[k]) * (i - stack[-1] - 1)
            stack.append(i)

        return ans


class SolutionPointer:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        ans = 0
        i, j = 0, len(height) - 1
        max_left, max_right = height[i], height[j]
        while i < j:
            if max_left < max_right:
                i += 1
                max_left = max(max_left, height[i])
                ans += max_left - height[i]
            else:
                j -= 1
                max_right = max(max_right, height[j])
                ans += max_right - height[j]

        return ans


if __name__ == '__main__':
    solution = Solution()

    answer = solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(answer, 6)

    answer = solution.trap([5, 4, 1, 2])
    print(answer, 1)

    answer = solution.trap([9, 6, 8, 8, 5, 6, 3])
    print(answer, 3)

    answer = solution.trap([8, 8, 1, 5, 6, 2, 5, 3, 3, 9])
    print(answer, 31)

    answer = solution.trap([4, 3, 3, 9, 3, 0, 9, 2, 8, 3])
    print(answer, 23)

    answer = solution.trap([])
    print(answer, 0)

    answer = solution.trap([1])
    print(answer, 0)

    answer = solution.trap([1, 2])
    print(answer, 0)

    answer = solution.trap([2, 1, 3])
    print(answer, 1)

    answer = solution.trap([0, 4, 1, 2, 3, 2, 1, 5, 1, 3, 1, 4, 1])
    print(answer, 18)

    answer = solution.trap([0, 4, 1, 2, 3, 2, 1, 5, 0, 5, 1, 3, 1, 4, 1])
    print(answer, 23)
