import java.util.Set;
import java.util.HashSet;
import java.util.Map;
import java.util.HashMap;

class Solution {
    public boolean isIsomorphic(String s, String t) {
        Map<Character, Character> m = new HashMap<>();
        Set<Character> st = new HashSet<>();
        for (int i = 0; i < s.length(); ++i) {
            Character c1 = s.charAt(i), c2 = t.charAt(i);
            if (m.containsKey(c1) && m.get(c1) != c2) return false;
            if (m.containsKey(c1) && m.get(c1) == c2) continue;
            if (st.contains(c2)) return false;
            m.put(c1, c2);
            st.add(c2);
        }
        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        boolean answer;

        answer = solution.isIsomorphic("egg", "add");
        System.out.printf("%b %b\n", answer, true);

        answer = solution.isIsomorphic("foo", "bar");
        System.out.printf("%b %b\n", answer, false);

        answer = solution.isIsomorphic("paper", "title");
        System.out.printf("%b %b\n", answer, true);

        answer = solution.isIsomorphic("", "");
        System.out.printf("%b %b\n", answer, true);

        answer = solution.isIsomorphic("a", "b");
        System.out.printf("%b %b\n", answer, true);

        answer = solution.isIsomorphic("ab", "bc");
        System.out.printf("%b %b\n", answer, true);

        answer = solution.isIsomorphic("abc", "abc");
        System.out.printf("%b %b\n", answer, true);

        answer = solution.isIsomorphic("abc", "aba");
        System.out.printf("%b %b\n", answer, false);

        answer = solution.isIsomorphic("aba", "abc");
        System.out.printf("%b %b\n", answer, false);
    }
}