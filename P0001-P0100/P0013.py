class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        rules = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                 (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        while s != "":
            for integer, roman in rules:
                if s.startswith(roman):
                    ans += integer
                    s = s[len(roman):]
                    break
        return ans


if __name__ == '__main__':
    solution = Solution()
    answer = solution.romanToInt("III")
    print(answer, 3)
    answer = solution.romanToInt("IV")
    print(answer, 4)
    answer = solution.romanToInt("IX")
    print(answer, 9)
    answer = solution.romanToInt("LVIII")
    print(answer, 58)
    answer = solution.romanToInt("MCMXCIV")
    print(answer, 1994)
