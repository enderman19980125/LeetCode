import java.util.Arrays;

class Solution {
    private int numLiveNeighbors(int[][] board, int x, int y) {
        int num = 0;
        int[] dx = new int[]{-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dy = new int[]{-1, 0, 1, -1, 1, -1, 0, 1};
        for (int k = 0; k < 8; ++k) {
            int xx = x + dx[k], yy = y + dy[k];
            if (0 <= xx && xx < board.length && 0 <= yy && yy < board[0].length && board[xx][yy] / 10 == 1) ++num;
        }
        return num;
    }

    public void gameOfLife(int[][] board) {
        int n = board.length, m = board[0].length;
        for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) board[i][j] *= 10;

        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j) {
                int num = numLiveNeighbors(board, i, j);
                if (board[i][j] / 10 == 1 && (num == 2 || num == 3)) ++board[i][j];
                if (board[i][j] / 10 == 0 && num == 3) ++board[i][j];
            }

        for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) board[i][j] %= 10;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] answer, stdAnswer;

        answer = new int[][]{{0, 1, 0}, {0, 0, 1}, {1, 1, 1}, {0, 0, 0}};
        stdAnswer = new int[][]{{0, 0, 0}, {1, 0, 1}, {0, 1, 1}, {0, 1, 0}};
        solution.gameOfLife(answer);
        System.out.printf("%b %s %s\n", Arrays.deepEquals(answer, stdAnswer), Arrays.deepToString(answer), Arrays.deepToString(stdAnswer));

        answer = new int[][]{{1, 1}, {1, 0}};
        stdAnswer = new int[][]{{1, 1}, {1, 1}};
        solution.gameOfLife(answer);
        System.out.printf("%b %s %s\n", Arrays.deepEquals(answer, stdAnswer), Arrays.deepToString(answer), Arrays.deepToString(stdAnswer));
    }
}