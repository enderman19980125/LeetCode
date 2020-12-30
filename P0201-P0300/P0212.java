import java.util.ArrayList;
import java.util.List;

class Solution {
    private int n, m;
    private char[][] board;
    private boolean[][] used;

    private final int[] dx = new int[]{0, 0, -1, 1};
    private final int[] dy = new int[]{-1, 1, 0, 0};

    private void clearUsedArray() {
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                used[i][j] = false;
    }

    private boolean search(int x, int y, int index, String word) {
        if (index == word.length()) return true;
        for (int k = 0; k < 4; ++k) {
            int xx = x + dx[k], yy = y + dy[k];
            if (xx < 0 || xx >= n || yy < 0 || yy >= m) continue;
            if (board[xx][yy] != word.charAt(index) || used[xx][yy]) continue;
            used[xx][yy] = true;
            boolean r = search(xx, yy, index + 1, word);
            used[xx][yy] = false;
            if (r) return true;
        }
        return false;
    }

    private boolean isFind(String word) {
        if (word.length() > n * m) return false;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j) {
                if (board[i][j] != word.charAt(0)) continue;
                clearUsedArray();
                used[i][j] = true;
                boolean r = search(i, j, 1, word);
                if (r) return true;
            }
        return false;
    }

    public List<String> findWords(char[][] board, String[] words) {
        this.n = board.length;
        this.m = board[0].length;
        this.board = board;
        used = new boolean[n][m];

        ArrayList<String> ans = new ArrayList<>();
        for (String word : words) if (isFind(word)) ans.add(word);
        return ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        char[][] board;
        String[] words;
        List<String> answer;

        board = convertBoard("oaan,etae,ihkr,iflv");
        words = convertWords("oath,pea,eat,rain");
        answer = solution.findWords(board, words);
        System.out.printf("%s %s\n", answer, "[eat, oath]");

        board = convertBoard("ab,cd");
        words = convertWords("abcb");
        answer = solution.findWords(board, words);
        System.out.printf("%s %s\n", answer, "[]");

        board = convertBoard("a");
        words = convertWords("a,b");
        answer = solution.findWords(board, words);
        System.out.printf("%s %s\n", answer, "[a]");

        board = convertBoard("abcd,efgh");
        words = convertWords("aefg,ab,aba,hgfeabcd,abcdefgh");
        answer = solution.findWords(board, words);
        System.out.printf("%s %s\n", answer, "[aefg, ab, hgfeabcd]");
    }

    private static char[][] convertBoard(String boardStr) {
        String[] rows = boardStr.split(",");
        char[][] board = new char[rows.length][rows[0].length()];
        for (int i = 0; i < rows.length; ++i)
            for (int j = 0; j < rows[0].length(); ++j)
                board[i][j] = rows[i].charAt(j);
        return board;
    }

    private static String[] convertWords(String wordsStr) {
        return wordsStr.split(",");
    }
}