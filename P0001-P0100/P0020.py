class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if c == ")" and len(stack) >= 1 and stack[-1] == "(":
                    stack.pop()
                elif c == "]" and len(stack) >= 1 and stack[-1] == "[":
                    stack.pop()
                elif c == "}" and len(stack) >= 1 and stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(c)
                    break
        return not stack


if __name__ == '__main__':
    solution = Solution()
    answer = solution.isValid("()")
    print(answer, True)
    answer = solution.isValid("()[]{}")
    print(answer, True)
    answer = solution.isValid("(]")
    print(answer, False)
    answer = solution.isValid("([)]")
    print(answer, False)
    answer = solution.isValid("{[]}")
    print(answer, True)
    answer = solution.isValid("]")
    print(answer, False)
