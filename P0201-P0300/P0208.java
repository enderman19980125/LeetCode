import java.util.Map;
import java.util.HashMap;

class Trie {

    private final Node root = new Node(' ');

    static class Node {
        char c;
        boolean isWord = false;
        Map<Character, Node> next = new HashMap<>();

        Node(char c) {
            this.c = c;
        }
    }

    /**
     * Initialize your data structure here.
     */
    public Trie() {
    }

    /**
     * Inserts a word into the trie.
     */
    public void insert(String word) {
        Node p = this.root;
        for (int i = 0; i < word.length(); ++i) {
            char c = word.charAt(i);
            if (!p.next.containsKey(c)) {
                p.next.put(c, new Node(c));
            }
            p = p.next.get(c);
        }
        p.isWord = true;
    }

    /**
     * Returns if the word is in the trie.
     */
    public boolean search(String word) {
        Node p = this.root;
        for (int i = 0; i < word.length(); ++i) {
            char c = word.charAt(i);
            if (!p.next.containsKey(c)) return false;
            p = p.next.get(c);
        }
        return p.isWord;
    }

    /**
     * Returns if there is any word in the trie that starts with the given prefix.
     */
    public boolean startsWith(String prefix) {
        Node p = this.root;
        for (int i = 0; i < prefix.length(); ++i) {
            char c = prefix.charAt(i);
            if (!p.next.containsKey(c)) return false;
            p = p.next.get(c);
        }
        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Trie trie = new Trie();
        boolean answer;

        trie.insert("apple");

        answer = trie.search("apple");
        System.out.printf("%b %b\n", answer, true);

        answer = trie.search("app");
        System.out.printf("%b %b\n", answer, false);

        answer = trie.startsWith("app");
        System.out.printf("%b %b\n", answer, true);

        trie.insert("app");

        answer = trie.search("app");
        System.out.printf("%b %b\n", answer, true);

        trie.insert("baby");

        answer = trie.search("baby");
        System.out.printf("%b %b\n", answer, true);

        answer = trie.startsWith("bab");
        System.out.printf("%b %b\n", answer, true);

        answer = trie.startsWith("babe");
        System.out.printf("%b %b\n", answer, false);
    }
}