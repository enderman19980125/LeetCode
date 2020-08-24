class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        pos = [-1 for _ in range(n)]
        for i in range(n):
            if i >= 1 and s[i - 1] == "(" and s[i] == ")":
                pos[i - 1] = 0
                pos[i] = 1

        while True:
            flag = False
            i = n - 1

            while i >= 0:
                if pos[i] > 0:
                    j = i
                    while (next_j := j - pos[j] - 1) >= 0 and pos[next_j] > 0:
                        j = next_j
                    j = j - pos[j]
                    if i - j != pos[i]:
                        pos[i] = i - j
                        flag = True
                    if j - 1 >= 0 and s[j - 1] == "(" and i + 1 < n and s[i + 1] == ")":
                        j -= 1
                        pos[j] = 0
                        pos[i + 1] = i - j + 1
                        flag = True
                    i = j

                i -= 1

            if not flag:
                break

        ans = max(pos) + 1
        return ans


class SolutionDP:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dp = [0 for _ in range(n)]
        for i in range(n):
            j = i - 1 - dp[i - 1]
            if i >= 1 and s[i] == ")" and s[i - 1] == ")" and j >= 0 and s[j] == "(":
                dp[i] = dp[i - 1] + dp[j - 1] + 2
            if i >= 1 and s[i] == ")" and s[i - 1] == "(":
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
        return max(dp)


class SolutionStack:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        ans = 0
        stack = [(-1, ")")]
        for i, c in enumerate(s):
            if c == ")" and len(stack) > 0 and stack[-1][1] == "(":
                stack.pop()
                ans = max(ans, i - stack[-1][0])
            else:
                stack.append((i, c))
        return ans


class SolutionPointer:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        ans = 0
        left, right = 0, 0
        for c in s:
            if c == "(":
                left += 1
            else:
                right += 1
            if left < right:
                left, right = 0, 0
            if left == right:
                ans = max(ans, left + right)

        left, right = 0, 0
        for c in reversed(s):
            if c == "(":
                left += 1
            else:
                right += 1
            if left > right:
                left, right = 0, 0
            if left == right:
                ans = max(ans, left + right)

        return ans


if __name__ == '__main__':
    solution = Solution()

    answer = solution.longestValidParentheses("(()")
    print(answer, 2)

    answer = solution.longestValidParentheses(")()())")
    print(answer, 4)

    answer = solution.longestValidParentheses("")
    print(answer, 0)

    answer = solution.longestValidParentheses("(")
    print(answer, 0)

    answer = solution.longestValidParentheses("()")
    print(answer, 2)

    answer = solution.longestValidParentheses(")(()(())))()")
    print(answer, 8)

    answer = solution.longestValidParentheses("(())()(())")
    print(answer, 10)

    answer = solution.longestValidParentheses("((())()(())")
    print(answer, 10)

    answer = solution.longestValidParentheses("(())()(()))")
    print(answer, 10)
