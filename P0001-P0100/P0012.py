class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        rules = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                 (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        while num > 0:
            for integer, roman in rules:
                if num >= integer:
                    num -= integer
                    ans += roman
                    break
        return ans


if __name__ == '__main__':
    solution = Solution()
    answer = solution.intToRoman(3)
    print(answer, "III")
    answer = solution.intToRoman(4)
    print(answer, "IV")
    answer = solution.intToRoman(9)
    print(answer, "IX")
    answer = solution.intToRoman(58)
    print(answer, "LVIII")
    answer = solution.intToRoman(1994)
    print(answer, "MCMXCIV")
