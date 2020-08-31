class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na, nb = len(a), len(b)
        if na < nb:
            a, b = b, a
            na, nb = nb, na
        b = "0" * (na - nb) + b

        ans = []
        m = 0
        for i in range(na - 1, -1, -1):
            k = int(a[i]) + int(b[i]) + m
            m = int(k >= 2)
            k = k % 2
            ans.append(k)
        if m == 1:
            ans.append(m)

        ans.reverse()
        ans = map(str, ans)
        ans = "".join(ans)
        return ans


if __name__ == '__main__':
    solution = Solution()

    answer = solution.addBinary("11", "1")
    print(answer, "100")

    answer = solution.addBinary("1010", "1011")
    print(answer, "10101")

    answer = solution.addBinary("0", "0")
    print(answer, "0")

    answer = solution.addBinary("0", "1")
    print(answer, "1")

    answer = solution.addBinary("1", "0")
    print(answer, "1")

    answer = solution.addBinary("1", "1")
    print(answer, "10")

    answer = solution.addBinary("11", "11")
    print(answer, "110")

    answer = solution.addBinary("10101", "1")
    print(answer, "10110")
