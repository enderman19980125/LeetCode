from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        i, j = 0, len(height) - 1
        while i < j:
            left, right = height[i], height[j]
            ans = max(ans, (j - i) * min(left, right))
            if left < right:
                while i < j and height[i] <= left:
                    i += 1
            else:
                while i < j and height[j] <= right:
                    j -= 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    answer = solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(answer, 49)
    answer = solution.maxArea([0, 7])
    print(answer, 0)
