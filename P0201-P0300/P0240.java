class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int N = matrix.length, M = matrix[0].length;
        int n = 0, m = M - 1;

        while (n < N) {
            if (matrix[n][M - 1] < target) {
                ++n;
                continue;
            }
            if (target < matrix[n][0]) {
                n = N;
                break;
            }

            int left = 0, right = m;
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (matrix[n][mid] < target) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }

            if (matrix[n][left] == target) break;
            if (target < matrix[n][left]) m = left - 1;
            ++n;
        }

        return n != N;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] matrix;
        boolean answer, stdAnswer;

        stdAnswer = true;
        matrix = new int[][]{{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19}, {3, 6, 9, 16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}};
        answer = solution.searchMatrix(matrix, 5);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = false;
        matrix = new int[][]{{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19}, {3, 6, 9, 16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}};
        answer = solution.searchMatrix(matrix, 20);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = true;
        matrix = new int[][]{{1}};
        answer = solution.searchMatrix(matrix, 1);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = false;
        matrix = new int[][]{{1}};
        answer = solution.searchMatrix(matrix, 0);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = true;
        matrix = new int[][]{{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19}, {3, 6, 9, 16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}};
        answer = solution.searchMatrix(matrix, 15);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = true;
        matrix = new int[][]{{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19}, {3, 6, 9, 16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}};
        answer = solution.searchMatrix(matrix, 1);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = true;
        matrix = new int[][]{{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19}, {3, 6, 9, 16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}};
        answer = solution.searchMatrix(matrix, 30);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = false;
        matrix = new int[][]{{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19}, {3, 6, 9, 16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}};
        answer = solution.searchMatrix(matrix, 0);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = false;
        matrix = new int[][]{{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19}, {3, 6, 9, 16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}};
        answer = solution.searchMatrix(matrix, 31);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = false;
        matrix = new int[][]{{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19}, {3, 6, 9, 16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}};
        answer = solution.searchMatrix(matrix, 20);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = false;
        matrix = new int[][]{{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19}, {3, 6, 9, 16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}};
        answer = solution.searchMatrix(matrix, 28);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = true;
        matrix = new int[][]{{3, 6, 9, 12, 17, 22}, {5, 11, 11, 16, 22, 26}, {10, 11, 14, 16, 24, 31}, {10, 15, 17, 17, 29, 31}, {14, 17, 20, 23, 34, 37}, {19, 21, 22, 28, 37, 40}, {22, 22, 24, 32, 37, 43}};
        answer = solution.searchMatrix(matrix, 20);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);
    }
}