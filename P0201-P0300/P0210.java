import java.util.*;

class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int k = 0;
        int[] ans = new int[numCourses];
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
                ans[k++] = p1;
                continue;
            }
            if (inDegree.isEmpty())
                return ans;
            else
                return new int[0];
        }

    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        ArrayList<Integer> nums = new ArrayList<>();
        int[] answer;

        Collections.addAll(nums, 1, 0);
        answer = solution.findOrder(2, arrayToIntArray(nums));
        System.out.printf("%s %s\n", intArrayToString(answer), "[0,1]");
        nums.clear();

        Collections.addAll(nums, 1, 0, 2, 0, 3, 1, 3, 2);
        answer = solution.findOrder(4, arrayToIntArray(nums));
        System.out.printf("%s %s\n", intArrayToString(answer), "[0,2,1,3]");
        nums.clear();

        answer = solution.findOrder(1, arrayToIntArray(nums));
        System.out.printf("%s %s\n", intArrayToString(answer), "[0]");
        nums.clear();

        Collections.addAll(nums, 1, 0, 2, 1, 3, 2);
        answer = solution.findOrder(4, arrayToIntArray(nums));
        System.out.printf("%s %s\n", intArrayToString(answer), "[0,1,2,3]");
        nums.clear();

        Collections.addAll(nums, 1, 0, 2, 1, 3, 2, 2, 3);
        answer = solution.findOrder(4, arrayToIntArray(nums));
        System.out.printf("%s %s\n", intArrayToString(answer), "[]");
        nums.clear();
    }

    private static int[][] arrayToIntArray(ArrayList<Integer> nums) {
        int n = nums.size();
        int[][] a = new int[n / 2][2];
        for (int i = 0; i < n; ++i) a[i / 2][i % 2] = nums.get(i);
        return a;
    }

    private static String intArrayToString(int[] nums) {
        if (nums.length == 0) return "[]";
        StringBuilder ans = new StringBuilder("[");
        for (int num : nums) ans.append(num).append(",");
        ans.delete(ans.length() - 1, ans.length());
        ans.append("]");
        return ans.toString();
    }
}