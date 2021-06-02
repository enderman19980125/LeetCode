import java.util.*;

class Solution {
    private final Map<Long, Integer> map = new HashMap<>();

    private boolean solutionGeneral(int[] nums, int k, int t) {
        map.clear();

        for (int i = 0; i < nums.length; i++) {
            long val = nums[i];
            for (long j = val - t; j <= val + t; j++) if (map.containsKey(j)) return true;

            map.put(val, map.getOrDefault(val, 0) + 1);

            int p = i - k;
            if (p >= 0) {
                val = nums[p];
                map.put(val, map.get(val) - 1);
                if (map.get(val) == 0) map.remove(val);
            }
        }

        return false;
    }

    private boolean solutionSmallT(int[] nums, int k, int t) {
        for (int i = 0; i < nums.length; i++)
            for (int j = i + 1; j <= i + k && j < nums.length; j++)
                if (Math.abs((long) nums[i] - (long) nums[j]) <= t) return true;
        return false;
    }

    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (t <= 10)
            return solutionSmallT(nums, k, t);
        else
            return solutionGeneral(nums, k, t);
    }
}

class SolutionTreeSet {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        TreeSet<Long> set = new TreeSet<>();
        for (int i = 0; i < nums.length; i++) {
            Long cntVal = (long) nums[i];
            Long oldVal = set.ceiling(cntVal - t);
            if (oldVal != null && Math.abs(cntVal - oldVal) <= t) return true;
            set.add(cntVal);
            if (i - k >= 0) set.remove((long) nums[i - k]);
        }
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums;
        int k, t;
        boolean answer, stdAnswer;

        nums = new int[]{1, 2, 3, 1};
        k = 3;
        t = 0;
        stdAnswer = true;
        answer = solution.containsNearbyAlmostDuplicate(nums, k, t);
        System.out.printf("%b %b %b\n", answer == stdAnswer, answer, stdAnswer);

        nums = new int[]{1, 0, 1, 1};
        k = 1;
        t = 2;
        stdAnswer = true;
        answer = solution.containsNearbyAlmostDuplicate(nums, k, t);
        System.out.printf("%b %b %b\n", answer == stdAnswer, answer, stdAnswer);

        nums = new int[]{1, 5, 9, 1, 5, 9};
        k = 2;
        t = 3;
        stdAnswer = false;
        answer = solution.containsNearbyAlmostDuplicate(nums, k, t);
        System.out.printf("%b %b %b\n", answer == stdAnswer, answer, stdAnswer);

        nums = new int[]{-2147483648, 2147483647};
        k = 1;
        t = 1;
        stdAnswer = false;
        answer = solution.containsNearbyAlmostDuplicate(nums, k, t);
        System.out.printf("%b %b %b\n", answer == stdAnswer, answer, stdAnswer);

        nums = new int[]{2147483640, 2147483641};
        k = 1;
        t = 100;
        stdAnswer = true;
        answer = solution.containsNearbyAlmostDuplicate(nums, k, t);
        System.out.printf("%b %b %b\n", answer == stdAnswer, answer, stdAnswer);
    }
}