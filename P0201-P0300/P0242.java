import java.util.*;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); ++i)
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
        for (int i = 0; i < t.length(); ++i)
            map.put(t.charAt(i), map.getOrDefault(t.charAt(i), 0) - 1);
        for (Map.Entry<Character, Integer> entry : map.entrySet())
            if (entry.getValue() != 0) return false;
        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        boolean answer, stdAnswer;

        stdAnswer = true;
        answer = solution.isAnagram("anagram", "nagaram");
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = false;
        answer = solution.isAnagram("rat", "car");
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = true;
        answer = solution.isAnagram("a", "a");
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = false;
        answer = solution.isAnagram("ab", "ac");
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);
    }
}