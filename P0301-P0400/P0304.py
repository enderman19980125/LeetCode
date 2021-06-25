from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.__prefix_matrix = []
        for i, row in enumerate(matrix):
            self.__prefix_matrix.append([])
            for j, cell in enumerate(row):
                if i == 0 and j == 0:
                    value = cell
                elif i == 0:
                    value = cell + self.__prefix_matrix[0][j - 1]
                elif j == 0:
                    value = cell + self.__prefix_matrix[i - 1][0]
                else:
                    value = cell + self.__prefix_matrix[i - 1][j] + self.__prefix_matrix[i][j - 1] - self.__prefix_matrix[i - 1][j - 1]
                self.__prefix_matrix[i].append(value)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        value = self.__prefix_matrix[row2][col2]

        if row1 == 0 and col1 == 0:
            pass
        elif row1 == 0:
            value -= self.__prefix_matrix[row2][col1 - 1]
        elif col1 == 0:
            value -= self.__prefix_matrix[row1 - 1][col2]
        else:
            value += self.__prefix_matrix[row1 - 1][col1 - 1] - self.__prefix_matrix[row2][col1 - 1] - self.__prefix_matrix[row1 - 1][col2]

        return value


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

def test() -> None:
    num_matrix = NumMatrix(
        [[3, 0, 1, 4, 2],
         [5, 6, 3, 2, 1],
         [1, 2, 0, 1, 5],
         [4, 1, 0, 1, 7],
         [1, 0, 3, 0, 5]]
    )

    answer = num_matrix.sumRegion(2, 1, 4, 3)
    std_answer = 8
    print("%s %s %s" % (answer == std_answer, answer, std_answer))

    answer = num_matrix.sumRegion(1, 1, 2, 2)
    std_answer = 11
    print("%s %s %s" % (answer == std_answer, answer, std_answer))

    answer = num_matrix.sumRegion(1, 2, 2, 4)
    std_answer = 12
    print("%s %s %s" % (answer == std_answer, answer, std_answer))

    answer = num_matrix.sumRegion(0, 0, 0, 0)
    std_answer = 3
    print("%s %s %s" % (answer == std_answer, answer, std_answer))

    answer = num_matrix.sumRegion(0, 0, 1, 1)
    std_answer = 14
    print("%s %s %s" % (answer == std_answer, answer, std_answer))

    answer = num_matrix.sumRegion(0, 1, 1, 1)
    std_answer = 6
    print("%s %s %s" % (answer == std_answer, answer, std_answer))

    answer = num_matrix.sumRegion(1, 0, 1, 1)
    std_answer = 11
    print("%s %s %s" % (answer == std_answer, answer, std_answer))


if __name__ == '__main__':
    test()
