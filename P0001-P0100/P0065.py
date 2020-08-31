class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip(" ")

        if (i := s.find("e")) >= 0:
            a, b = s[:i], s[i + 1:]
        else:
            a, b = s, "0"

        if a.startswith("+") or a.startswith("-"):
            a = a[1:]
        if b.startswith("+") or b.startswith("-"):
            b = b[1:]

        if a == "" or b == "":
            return False
        if (i := a.find(".")) >= 0:
            a0, a1 = a[:i], a[i + 1:]
        else:
            a0, a1 = a, "0"
        if b.find(".") >= 0:
            return False

        if a0 == "" and a1.isnumeric() and b.isnumeric():
            return True
        if a0.isnumeric() and a1 == "" and b.isnumeric():
            return True
        if a0.isnumeric() and a1.isnumeric() and b.isnumeric():
            return True
        return False


if __name__ == '__main__':
    solution = Solution()

    answer = solution.isNumber("0")
    print(answer, True)

    answer = solution.isNumber(" 0.1 ")
    print(answer, True)

    answer = solution.isNumber("abc")
    print(answer, False)

    answer = solution.isNumber("1 a")
    print(answer, False)

    answer = solution.isNumber("2e10")
    print(answer, True)

    answer = solution.isNumber(" -90e3")
    print(answer, True)

    answer = solution.isNumber(" 1e")
    print(answer, False)

    answer = solution.isNumber("e3")
    print(answer, False)

    answer = solution.isNumber(" 6e-1")
    print(answer, True)

    answer = solution.isNumber(" 99e2.5")
    print(answer, False)

    answer = solution.isNumber("53.5e93")
    print(answer, True)

    answer = solution.isNumber(" --6 ")
    print(answer, False)

    answer = solution.isNumber("-+3")
    print(answer, False)

    answer = solution.isNumber("95a54e53")
    print(answer, False)

    answer = solution.isNumber(".1")
    print(answer, True)

    answer = solution.isNumber("3.")
    print(answer, True)

    answer = solution.isNumber(".")
    print(answer, False)

    answer = solution.isNumber("..")
    print(answer, False)

    answer = solution.isNumber("1e")
    print(answer, False)

    answer = solution.isNumber("e1")
    print(answer, False)
