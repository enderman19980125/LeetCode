class Solution:
    def myAtoi(self, str: str) -> int:
        int_max = 2 ** 31 - 1
        int_min = -2 ** 31
        ans = 0
        symbol = None
        is_start = False
        for c in str:
            if c == " " and not is_start:
                continue
            elif c in ["+", "-"] and symbol is None and not is_start:
                symbol = c
                is_start = True
            elif "0" <= c <= "9":
                ans = 10 * ans + int(c)
                is_start = True
            else:
                break
        ans *= 1 if symbol in [None, "+"] else -1
        ans = max(min(ans, int_max), int_min)
        return ans


if __name__ == '__main__':
    solution = Solution()
    answer = solution.myAtoi("42")
    print(answer, 42)
    answer = solution.myAtoi("   -42")
    print(answer, -42)
    answer = solution.myAtoi("4193 with words")
    print(answer, 4193)
    answer = solution.myAtoi("words and 987")
    print(answer, 0)
    answer = solution.myAtoi("-91283472332")
    print(answer, -2147483648)
    answer = solution.myAtoi("+2")
    print(answer, 2)
    answer = solution.myAtoi("+-2")
    print(answer, 0)
    answer = solution.myAtoi("   +0 123")
    print(answer, 0)
    answer = solution.myAtoi("0-1")
    print(answer, 0)
    answer = solution.myAtoi("-5-")
    print(answer, -5)
    answer = solution.myAtoi("-   234")
    print(answer, 0)
