import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

class WordDictionary {

    private final ArrayList<Set<String>> setArrayList = new ArrayList<>(501);

    /**
     * Initialize your data structure here.
     */
    public WordDictionary() {
        for (int i = 0; i <= 500; i++) setArrayList.add(i, new HashSet<String>());
    }

    /**
     * Adds a word into the data structure.
     */
    public void addWord(String word) {
        setArrayList.get(word.length()).add(word);
    }

    /**
     * Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
     */
    public boolean search(String word) {
        Set<String> set = setArrayList.get(word.length());
        if (!word.contains(".")) return set.contains(word);
        for (String s : set) {
            if (s.length() != word.length()) continue;
            boolean f = true;
            for (int i = 0; i < s.length(); ++i)
                if (word.charAt(i) != '.' && word.charAt(i) != s.charAt(i)) {
                    f = false;
                    break;
                }
            if (f) return true;
        }
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        WordDictionary wordDictionary = new WordDictionary();
        boolean answer;

        wordDictionary.addWord("bad");

        wordDictionary.addWord("dad");

        wordDictionary.addWord("mad");

        answer = wordDictionary.search("pad");
        System.out.printf("%b %b\n", answer, false);

        answer = wordDictionary.search("bad");
        System.out.printf("%b %b\n", answer, true);

        answer = wordDictionary.search(".ad");
        System.out.printf("%b %b\n", answer, true);

        answer = wordDictionary.search("b..");
        System.out.printf("%b %b\n", answer, true);
    }
}