from typing import List


class Solution:
    def __init__(self):
        self.used = []
        self.left_border = []
        self.right_border = []

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        min_value = min([interval[0] for interval in intervals])
        max_value = max([interval[1] for interval in intervals])
        offset = -min_value
        intervals = [[left + offset, right + offset] for left, right in intervals]
        self.used = [False for _ in range(max_value + offset + 1)]
        self.left_border = [i for i in range(max_value + offset + 1)]
        self.right_border = [i for i in range(max_value + offset + 1)]

        for left, right in intervals:
            left_l, left_r = self.find_left(left), self.find_right(left)
            right_l, right_r = self.find_left(right), self.find_right(right)
            for k in range(left_r, right_l + 1):
                self.used[k] = True
                self.left_border[k] = left_l
                self.right_border[k] = right_r

        ans = []
        k = 0
        while k <= max_value + offset:
            while k < max_value and not self.used[k]:
                k += 1
            left, right = self.find_left(k), self.find_right(k)
            ans.append([left - offset, right - offset])
            k = right + 1

        return ans

    def find_left(self, k: int) -> int:
        if self.left_border[k] != k:
            self.left_border[k] = self.find_left(self.left_border[k])
        return self.left_border[k]

    def find_right(self, k: int) -> int:
        if self.right_border[k] != k:
            self.right_border[k] = self.find_right(self.right_border[k])
        return self.right_border[k]


if __name__ == '__main__':
    solution = Solution()

    answer = solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    print(answer, [[1, 6], [8, 10], [15, 18]])

    answer = solution.merge([[1, 4], [4, 5]])
    print(answer, [[1, 5]])

    answer = solution.merge([])
    print(answer, [])

    answer = solution.merge([[2, 8]])
    print(answer, [[2, 8]])

    answer = solution.merge([[2, 4], [3, 5]])
    print(answer, [[2, 5]])

    answer = solution.merge([[3, 5], [2, 4]])
    print(answer, [[2, 5]])

    answer = solution.merge([[3, 4], [2, 5]])
    print(answer, [[2, 5]])

    answer = solution.merge([[2, 5], [3, 4]])
    print(answer, [[2, 5]])

    answer = solution.merge([[2, 5], [6, 9], [5, 6]])
    print(answer, [[2, 9]])

    answer = solution.merge([[2, 5], [6, 9], [4, 7]])
    print(answer, [[2, 9]])
