class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]
        ans_list = [0 for _ in range(len(num1) + len(num2))]
        for i, d1 in enumerate(num1):
            for j, d2 in enumerate(num2):
                d1, d2 = int(d1), int(d2)
                ans_list[i + j] += d1 * d2
                for k, d in enumerate(ans_list):
                    if d >= 10:
                        ans_list[k] = d % 10
                        ans_list[k + 1] += d // 10

        ans_list = map(str, reversed(ans_list))
        ans = "".join(ans_list)
        ans = ans.lstrip("0")
        ans = "0" if ans == "" else ans
        return ans


if __name__ == '__main__':
    solution = Solution()

    answer = solution.multiply("2", "3")
    print(answer, 6)

    answer = solution.multiply("123", "456")
    print(answer, "56088")

    answer = solution.multiply("0", "0")
    print(answer, 0)

    answer = solution.multiply("0", "888")
    print(answer, 0)

    answer = solution.multiply("888", "0")
    print(answer, 0)

    answer = solution.multiply("9999999999", "9999999999")
    print(answer, 99999999980000000001)
