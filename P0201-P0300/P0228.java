import java.util.*;

class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> ranges = new LinkedList<>();
        Integer s = null, t = null;

        for (int num : nums) {
            if (s == null) {
                s = num;
                t = num;
                continue;
            }
            if (t + 1 == num) {
                t = num;
                continue;
            }
            if (s.equals(t))
                ranges.add(s.toString());
            else
                ranges.add(String.format("%s->%s", s, t));
            s = num;
            t = num;
        }

        if (s != null) {
            if (s.equals(t))
                ranges.add(s.toString());
            else
                ranges.add(String.format("%s->%s", s, t));
        }

        return ranges;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums;
        List<String> answer, stdAnswer;

        nums = new int[]{0, 1, 2, 4, 5, 7};
        stdAnswer = Arrays.asList("0->2", "4->5", "7");
        answer = solution.summaryRanges(nums);
        System.out.printf("%b %s %s\n", answer.toString().equals(stdAnswer.toString()), answer, stdAnswer);

        nums = new int[]{0, 2, 3, 4, 6, 8, 9};
        stdAnswer = Arrays.asList("0", "2->4", "6", "8->9");
        answer = solution.summaryRanges(nums);
        System.out.printf("%b %s %s\n", answer.toString().equals(stdAnswer.toString()), answer, stdAnswer);

        nums = new int[]{};
        stdAnswer = new ArrayList<>();
        answer = solution.summaryRanges(nums);
        System.out.printf("%b %s %s\n", answer.toString().equals(stdAnswer.toString()), answer, stdAnswer);

        nums = new int[]{-1};
        stdAnswer = Collections.singletonList("-1");
        answer = solution.summaryRanges(nums);
        System.out.printf("%b %s %s\n", answer.toString().equals(stdAnswer.toString()), answer, stdAnswer);

        nums = new int[]{0};
        stdAnswer = Collections.singletonList("0");
        answer = solution.summaryRanges(nums);
        System.out.printf("%b %s %s\n", answer.toString().equals(stdAnswer.toString()), answer, stdAnswer);

        nums = new int[]{-3, -2, -1, 0, 1, 2, 3};
        stdAnswer = Collections.singletonList("-3->3");
        answer = solution.summaryRanges(nums);
        System.out.printf("%b %s %s\n", answer.toString().equals(stdAnswer.toString()), answer, stdAnswer);

        nums = new int[]{-3, -2, -1, 1, 2, 3};
        stdAnswer = Arrays.asList("-3->-1", "1->3");
        answer = solution.summaryRanges(nums);
        System.out.printf("%b %s %s\n", answer.toString().equals(stdAnswer.toString()), answer, stdAnswer);
    }
}