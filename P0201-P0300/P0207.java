import java.util.*;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, Integer> inDegree = new HashMap<>();
        ArrayList<Set<Integer>> outEdges = new ArrayList<>(numCourses);
        for (int i = 0; i < numCourses; ++i) {
            inDegree.put(i, 0);
            outEdges.add(i, new HashSet<>());
        }
        for (int[] p : prerequisites) {
            int p2 = p[0], p1 = p[1];
            outEdges.get(p1).add(p2);
            inDegree.put(p2, inDegree.get(p2) + 1);
        }
        while (true) {
            int p1 = -1;
            for (Map.Entry<Integer, Integer> entry : inDegree.entrySet())
                if (entry.getValue() == 0) {
                    p1 = entry.getKey();
                    for (int p2 : outEdges.get(p1)) inDegree.put(p2, inDegree.get(p2) - 1);
                    break;
                }
            if (p1 != -1) {
                inDegree.remove(p1);
                continue;
            }
            return inDegree.isEmpty();
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        ArrayList<Integer> nums = new ArrayList<>();
        boolean answer;

        Collections.addAll(nums, 1, 0);
        answer = solution.canFinish(2, arrayToIntArray(nums));
        System.out.printf("%b %b\n", answer, true);
        nums.clear();

        Collections.addAll(nums, 1, 0, 0, 1);
        answer = solution.canFinish(2, arrayToIntArray(nums));
        System.out.printf("%b %b\n", answer, false);
        nums.clear();

        answer = solution.canFinish(1, arrayToIntArray(nums));
        System.out.printf("%b %b\n", answer, true);
        nums.clear();

        Collections.addAll(nums, 1, 0, 2, 1);
        answer = solution.canFinish(3, arrayToIntArray(nums));
        System.out.printf("%b %b\n", answer, true);
        nums.clear();

        Collections.addAll(nums, 1, 0, 2, 1, 2, 0);
        answer = solution.canFinish(3, arrayToIntArray(nums));
        System.out.printf("%b %b\n", answer, true);
        nums.clear();

        Collections.addAll(nums, 1, 0, 2, 1, 1, 2);
        answer = solution.canFinish(3, arrayToIntArray(nums));
        System.out.printf("%b %b\n", answer, false);
        nums.clear();

        Collections.addAll(nums, 1, 0, 2, 1, 0, 2);
        answer = solution.canFinish(3, arrayToIntArray(nums));
        System.out.printf("%b %b\n", answer, false);
        nums.clear();
    }

    private static int[][] arrayToIntArray(ArrayList<Integer> nums) {
        int n = nums.size();
        int[][] a = new int[n / 2][2];
        for (int i = 0; i < n; ++i) a[i / 2][i % 2] = nums.get(i);
        return a;
    }
}