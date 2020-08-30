from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        is_insert = False
        for interval in intervals:
            if interval[1] < newInterval[0]:
                ans.append(interval)
            elif newInterval[1] < interval[0]:
                if not is_insert:
                    ans.append(newInterval)
                    is_insert = True
                ans.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        if not is_insert:
            ans.append(newInterval)
        return ans


if __name__ == '__main__':
    solution = Solution()

    answer = solution.insert([[1, 3], [6, 9]], [2, 5])
    print(answer, [[1, 5], [6, 9]])

    answer = solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
    print(answer, [[1, 2], [3, 10], [12, 16]])

    answer = solution.insert([[1, 3], [6, 9]], [2, 5])
    print(answer, [[1, 5], [6, 9]])

    answer = solution.insert([], [1, 2])
    print(answer, [[1, 2]])

    answer = solution.insert([[1, 2]], [3, 4])
    print(answer, [[1, 2], [3, 4]])

    answer = solution.insert([[3, 4]], [1, 2])
    print(answer, [[1, 2], [3, 4]])

    answer = solution.insert([[1, 2], [5, 6]], [3, 4])
    print(answer, [[1, 2], [3, 4], [5, 6]])

    answer = solution.insert([[1, 2], [5, 6]], [2, 5])
    print(answer, [[1, 6]])
