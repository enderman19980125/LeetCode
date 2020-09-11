# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return f"cnt = {self.val} & " \
               f"left = {self.left.val if self.left else None} & " \
               f"right = {self.right.val if self.right else None}"


class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][i] = 1
        for width in range(2, n + 1):
            for left in range(1, n - width + 2):
                right = left + width - 1
                dp[left][right] = dp[left + 1][right] + dp[left][right - 1]
                for k in range(left + 1, right):
                    dp[left][right] += dp[left][k - 1] * dp[k + 1][right]
        return dp[1][n]


if __name__ == '__main__':
    solution = Solution()

    answer = solution.numTrees(0)
    print(answer, 0)

    answer = solution.numTrees(1)
    print(answer, 1)

    answer = solution.numTrees(2)
    print(answer, 2)

    answer = solution.numTrees(3)
    print(answer, 5)

    answer = solution.numTrees(4)
    print(answer, 14)

    answer = solution.numTrees(5)
    print(answer, 42)

    answer = solution.numTrees(6)
    print(answer, 132)
