class Solution {
    public int maximalSquare(char[][] matrix) {
        int n = matrix.length, m = matrix[0].length;
        int[][] sum = new int[n + 1][m + 1];
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++) {
                sum[i][j] = matrix[i - 1][j - 1] - '0';
                if (i == 1 && j != 1) sum[i][j] += sum[i][j - 1];
                if (i != 1 && j == 1) sum[i][j] += sum[i - 1][j];
                if (i != 1 && j != 1) sum[i][j] += sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1];
            }

        int maxArea = 0;
        for (int x1 = 1; x1 <= n; x1++)
            for (int y1 = 1; y1 <= m; y1++)
                for (int side = 1; x1 + side - 1 <= n && y1 + side - 1 <= m; side++) {
                    int x2 = x1 + side - 1;
                    int y2 = y1 + side - 1;
                    if (sum[x2][y2] - sum[x1 - 1][y2] - sum[x2][y1 - 1] + sum[x1 - 1][y1 - 1] == (x2 - x1 + 1) * (y2 - y1 + 1))
                        maxArea = Math.max(maxArea, side * side);
                    else
                        break;
                }

        return maxArea;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        char[][] nums;
        int answer, stdAnswer;

        nums = new char[][]{
                {'1', '0', '1', '0', '0'},
                {'1', '0', '1', '1', '1'},
                {'1', '1', '1', '1', '1'},
                {'1', '0', '0', '1', '0'}
        };
        stdAnswer = 4;
        answer = solution.maximalSquare(nums);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        nums = new char[][]{{'0', '1'}, {'1', '0'}};
        stdAnswer = 1;
        answer = solution.maximalSquare(nums);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        nums = new char[][]{{'0'}};
        stdAnswer = 0;
        answer = solution.maximalSquare(nums);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        nums = new char[][]{{'1'}};
        stdAnswer = 1;
        answer = solution.maximalSquare(nums);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        nums = new char[][]{
                {'1', '0', '1', '0', '0'},
                {'0', '0', '1', '1', '1'},
                {'1', '1', '1', '1', '1'},
                {'0', '0', '1', '1', '1'}
        };
        stdAnswer = 9;
        answer = solution.maximalSquare(nums);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);
    }
}