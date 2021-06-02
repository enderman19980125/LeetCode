import java.util.*;

class Solution {
    public int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        if (ax2 <= bx1 || bx2 <= ax1 || ay2 <= by1 || by2 <= ay1)
            return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1);

        TreeMap<Double, int[]> xTM = new TreeMap<>();
        xTM.put(ax1 - 0.1, new int[]{-1, ay1, ay2});
        xTM.put(ax2 - 0.1, new int[]{1, ay1, ay2});
        xTM.put(bx1 + 0.1, new int[]{-1, by1, by2});
        xTM.put(bx2 + 0.1, new int[]{1, by1, by2});

        int area = 0;
        Integer xPre = null;
        TreeMap<Integer, Integer> yTS = new TreeMap<>();

        for (Map.Entry<Double, int[]> e : xTM.entrySet()) {
            int xCnt = (int) Math.round(e.getKey());
            if (xPre != null && yTS.size() != 0) {
                int yMin = yTS.firstKey(), yMax = yTS.lastKey();
                area += (yMax - yMin) * (xCnt - xPre);
            }

            int y;
            if (e.getValue()[0] == -1) {
                y = e.getValue()[1];
                yTS.put(y, yTS.getOrDefault(y, 0) + 1);
                y = e.getValue()[2];
                yTS.put(y, yTS.getOrDefault(y, 0) + 1);
            } else {
                y = e.getValue()[1];
                yTS.put(y, yTS.getOrDefault(y, 0) - 1);
                if (yTS.get(y) == 0) yTS.remove(y);
                y = e.getValue()[2];
                yTS.put(y, yTS.getOrDefault(y, 0) - 1);
                if (yTS.get(y) == 0) yTS.remove(y);
            }

            xPre = xCnt;
        }

        return area;
    }
}

class SolutionCross {
    public int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        if (bx1 < ax1) {
            int t;
            t = ax1;
            ax1 = bx1;
            bx1 = t;
            t = ax2;
            ax2 = bx2;
            bx2 = t;
            t = ay1;
            ay1 = by1;
            by1 = t;
            t = ay2;
            ay2 = by2;
            by2 = t;
        }

        int area = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1);
        if (ax2 <= bx1 || ay2 <= by1 || by2 <= ay1) return area;

        int x1 = bx1, x2 = Math.min(ax2, bx2);
        int y1 = Math.max(ay1, by1), y2 = Math.min(ay2, by2);
        return area - (x2 - x1) * (y2 - y1);
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int answer, stdAnswer;

        stdAnswer = 45;
        answer = solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 16;
        answer = solution.computeArea(-2, -2, 2, 2, -2, -2, 2, 2);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 8;
        answer = solution.computeArea(-2, 0, 0, 2, 0, -1, 2, 1);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 8;
        answer = solution.computeArea(-2, 0, 0, 2, 1, -1, 3, 1);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 8;
        answer = solution.computeArea(-2, 0, 0, 2, -2, 4, 0, 6);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 12;
        answer = solution.computeArea(-1, 0, 1, 4, -2, 1, 2, 3);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 58;
        answer = solution.computeArea(-5, -5, 0, 3, -3, -3, 3, 3);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 42;
        answer = solution.computeArea(-3, -5, 0, 3, -3, -3, 3, 3);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 41;
        answer = solution.computeArea(4, -5, 5, 0, -3, -3, 3, 3);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);
    }
}