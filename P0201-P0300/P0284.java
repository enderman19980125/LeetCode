import java.util.*;

// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html

class PeekingIterator implements Iterator<Integer> {
    private final Iterator<Integer> iterator;
    private Integer value = null;

    public PeekingIterator(Iterator<Integer> iterator) {
        // initialize any member here.
        this.iterator = iterator;
    }

    // Returns the next element in the iteration without advancing the iterator.
    public Integer peek() {
        if (value != null) {
            return value;
        }
        value = iterator.next();
        return value;
    }

    // hasNext() and next() should behave the same as in the Iterator interface.
    // Override them if needed.
    @Override
    public Integer next() {
        if (value != null) {
            int p = value;
            value = null;
            return p;
        }
        return iterator.next();
    }

    @Override
    public boolean hasNext() {
        return value != null || iterator.hasNext();
    }
}

public class Main {
    public static void main(String[] args) {
        Iterator<Integer> iterator = List.of(1, 2, 3).iterator();
        PeekingIterator peekingIterator = new PeekingIterator(iterator);
        Integer answer, stdAnswer;

        stdAnswer = 1;
        answer = peekingIterator.next();
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        stdAnswer = 2;
        answer = peekingIterator.peek();
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        stdAnswer = 2;
        answer = peekingIterator.next();
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        stdAnswer = 3;
        answer = peekingIterator.next();
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        stdAnswer = 0;
        answer = peekingIterator.hasNext() ? 1 : 0;
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);
    }
}