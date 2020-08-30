class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        for i in range(1, 10):
            factorial.append(factorial[-1] * i)

        used = []
        for pos in range(1, n + 1):
            i, num = 1, 1
            for num in range(1, n + 1):
                if num in used:
                    continue
                elif i * factorial[n - pos] < k:
                    i += 1
                    continue
                else:
                    break
            used.append(num)
            k -= (i - 1) * factorial[n - pos]

        ans = "".join(map(str, used))
        return ans


if __name__ == '__main__':
    solution = Solution()

    answer = solution.getPermutation(3, 3)
    print(answer, "213")

    answer = solution.getPermutation(4, 9)
    print(answer, "2314")

    answer = solution.getPermutation(1, 1)
    print(answer, "1")

    answer = solution.getPermutation(2, 1)
    print(answer, "12")

    answer = solution.getPermutation(2, 2)
    print(answer, "21")

    answer = solution.getPermutation(3, 1)
    print(answer, "123")

    answer = solution.getPermutation(3, 2)
    print(answer, "132")

    answer = solution.getPermutation(3, 3)
    print(answer, "213")

    answer = solution.getPermutation(3, 4)
    print(answer, "231")

    answer = solution.getPermutation(3, 5)
    print(answer, "312")

    answer = solution.getPermutation(3, 6)
    print(answer, "321")
