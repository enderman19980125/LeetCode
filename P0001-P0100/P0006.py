class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [[] for _ in range(numRows)]
        row, direction = 0, 1
        for c in s:
            matrix[row].append(c)
            if numRows == 1:
                continue
            if row == numRows - 1 and direction == 1:
                direction = -1
            if row == 0 and direction == -1:
                direction = 1
            row += direction
        ans = "".join(["".join([c for c in row_list]) for row_list in matrix])
        return ans


if __name__ == '__main__':
    solution = Solution()
    answer = solution.convert("PAYPALISHIRING", 3)
    print(answer, "PAHNAPLSIIGYIR")
    answer = solution.convert("PAYPALISHIRING", 4)
    print(answer, "PINALSIGYAHRPI")
    answer = solution.convert("PAYPALISHIRING", 1)
    print(answer, "PAYPALISHIRING")
