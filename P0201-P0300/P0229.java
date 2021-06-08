import java.util.*;

class Solution {
    public List<Integer> majorityElement(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        List<Integer> ans = new LinkedList<>();

        for (int num : nums) map.put(num, map.getOrDefault(num, 0) + 1);

        for (Map.Entry<Integer, Integer> e : map.entrySet())
            if (e.getValue() > 1.0 * nums.length / 3) ans.add(e.getKey());

        return ans;
    }
}

class SolutionBoyerMoore {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> ans = new LinkedList<>();
        if (nums.length == 0) return ans;
        if (nums.length == 1) {
            ans.add(nums[0]);
            return ans;
        }

        int a1 = Integer.MAX_VALUE, a2 = Integer.MAX_VALUE, n1 = 0, n2 = 0;

        for (int num : nums) {
            if (a1 == num) {
                ++n1;
                continue;
            }
            if (a2 == num) {
                ++n2;
                continue;
            }
            if (n1 == 0) {
                a1 = num;
                n1 = 1;
                continue;
            }
            if (n2 == 0) {
                a2 = num;
                n2 = 1;
                continue;
            }
            --n1;
            --n2;
        }

        int c1 = 0, c2 = 0;
        for (int num : nums) {
            if (n1 >= 0 && a1 == num) ++c1;
            if (n2 >= 0 && a2 == num) ++c2;
        }

        if (c1 > Math.floor(1.0 * nums.length / 3)) ans.add(a1);
        if (c2 > Math.floor(1.0 * nums.length / 3) && !Objects.equals(a1, a2)) ans.add(a2);

        return ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums;
        List<Integer> answer, stdAnswer;

        nums = new int[]{3, 2, 3};
        stdAnswer = Collections.singletonList(3);
        answer = solution.majorityElement(nums);
        System.out.printf("%b %s %s\n", answer.toString().equals(stdAnswer.toString()), answer, stdAnswer);

        nums = new int[]{1};
        stdAnswer = Collections.singletonList(1);
        answer = solution.majorityElement(nums);
        System.out.printf("%b %s %s\n", answer.toString().equals(stdAnswer.toString()), answer, stdAnswer);

        nums = new int[]{1, 2};
        stdAnswer = Arrays.asList(1, 2);
        answer = solution.majorityElement(nums);
        System.out.printf("%b %s %s\n", answer.toString().equals(stdAnswer.toString()), answer, stdAnswer);

        nums = new int[]{1, 1, 2, 2, 3, 3};
        stdAnswer = new LinkedList<>();
        answer = solution.majorityElement(nums);
        System.out.printf("%b %s %s\n", answer.toString().equals(stdAnswer.toString()), answer, stdAnswer);

        nums = new int[]{1, 1, 1, 2, 2, 2};
        stdAnswer = Arrays.asList(1, 2);
        answer = solution.majorityElement(nums);
        System.out.printf("%b %s %s\n", answer.toString().equals(stdAnswer.toString()), answer, stdAnswer);

        nums = new int[]{1, 2, 1, 2, 1, 2};
        stdAnswer = Arrays.asList(1, 2);
        answer = solution.majorityElement(nums);
        System.out.printf("%b %s %s\n", answer.toString().equals(stdAnswer.toString()), answer, stdAnswer);

        nums = new int[]{2, 1, 1, 3, 1, 4, 5, 6};
        stdAnswer = Collections.singletonList(1);
        answer = solution.majorityElement(nums);
        System.out.printf("%b %s %s\n", answer.toString().equals(stdAnswer.toString()), answer, stdAnswer);

        nums = new int[]{1, 1, 1, 2, 3, 7, 8, 1, 6, 9};
        stdAnswer = Collections.singletonList(1);
        answer = solution.majorityElement(nums);
        System.out.printf("%b %s %s\n", answer.toString().equals(stdAnswer.toString()), answer, stdAnswer);

        nums = new int[]{4, 5, 3, 4, 4, 1, 0, -1, -2, 4, 6, 7, 8, 4};
        stdAnswer = Collections.singletonList(4);
        answer = solution.majorityElement(nums);
        System.out.printf("%b %s %s\n", answer.toString().equals(stdAnswer.toString()), answer, stdAnswer);

        nums = new int[]{4, 2, 1, 1};
        stdAnswer = Collections.singletonList(1);
        answer = solution.majorityElement(nums);
        System.out.printf("%b %s %s\n", answer.toString().equals(stdAnswer.toString()), answer, stdAnswer);

        nums = new int[]{1, 1, 2, 3, 4, 1, 1, 5, 6, 7, 1, 1, 8, 9, 10, 1, 11, 12, 13, 14};
        stdAnswer = Collections.singletonList(1);
        answer = solution.majorityElement(nums);
        System.out.printf("%b %s %s\n", answer.toString().equals(stdAnswer.toString()), answer, stdAnswer);
    }
}