from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.ans = []
        if n > 0:
            self._generate(0, 0, "")
        return self.ans

    def _generate(self, n_left: int, n_right: int, s: str):
        if n_left == n_right == self.n:
            self.ans.append(s)
            return
        if n_left < self.n:
            self._generate(n_left + 1, n_right, s + "(")
        if n_left > n_right:
            self._generate(n_left, n_right + 1, s + ")")


if __name__ == '__main__':
    solution = Solution()
    answer = solution.generateParenthesis(3)
    print(answer)
    print(["((()))", "(()())", "(())()", "()(())", "()()()"])
    answer = solution.generateParenthesis(1)
    print(answer)
    print(["()"])
    answer = solution.generateParenthesis(0)
    print(answer)
    print([])
