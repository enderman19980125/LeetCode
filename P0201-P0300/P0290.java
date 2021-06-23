import java.util.*;

class Solution {
    public boolean wordPattern(String pattern, String s) {
        HashMap<Character, String> hashMap1 = new HashMap<>();
        HashMap<String, Character> hashMap2 = new HashMap<>();
        StringTokenizer stringTokenizer = new StringTokenizer(s, " ");
        int k = -1;

        while (k + 1 < pattern.length() && stringTokenizer.hasMoreTokens()) {
            Character p = pattern.charAt(++k);
            String t = stringTokenizer.nextToken();
            if (hashMap1.containsKey(p) && !hashMap1.get(p).equals(t)) return false;
            if (hashMap2.containsKey(t) && hashMap2.get(t) != p) return false;
            hashMap1.put(p, t);
            hashMap2.put(t, p);
        }

        return k + 1 == pattern.length() && !stringTokenizer.hasMoreTokens();
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        boolean answer, stdAnswer;

        stdAnswer = true;
        answer = solution.wordPattern("abba", "dog cat cat dog");
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = false;
        answer = solution.wordPattern("abba", "dog cat cat fish");
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = false;
        answer = solution.wordPattern("aaaa", "dog cat cat dog");
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = false;
        answer = solution.wordPattern("abba", "dog dog dog dog");
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = false;
        answer = solution.wordPattern("aaa", "aa aa aa aa");
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = false;
        answer = solution.wordPattern("aaaa", "aa aa aa");
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);
    }
}