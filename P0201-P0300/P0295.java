import java.util.*;

class MedianFinder {
    private final PriorityQueue<Integer> q1, q2;

    /**
     * initialize your data structure here.
     */
    public MedianFinder() {
        q1 = new PriorityQueue<>();
        q2 = new PriorityQueue<>();
    }

    public void addNum(int num) {
        if (q2.isEmpty() || q2.peek() <= num)
            q2.add(num);
        else
            q1.add(-num);

        if (!q2.isEmpty() && q1.size() + 1 < q2.size())
            q1.add(-q2.poll());
        if (!q2.isEmpty() && q1.size() > q2.size())
            q2.add(-q1.poll());
    }

    public double findMedian() {
        assert !q2.isEmpty();
        if (q1.size() < q2.size())
            return q2.peek();
        else
            return (q2.peek() - q1.peek()) / 2.0;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */

public class Main {
    public static void main(String[] args) {
        double stdAnswer;
        MedianFinder medianFinder;

        medianFinder = new MedianFinder();
        medianFinder.addNum(1);
        medianFinder.addNum(2);
        stdAnswer = 1.5;
        medianFinder.findMedian();
        System.out.printf("%b %s %s\n", medianFinder.findMedian() == stdAnswer, medianFinder.findMedian(), stdAnswer);
        medianFinder.addNum(3);
        stdAnswer = 2.0;
        medianFinder.findMedian();
        System.out.printf("%b %s %s\n", medianFinder.findMedian() == stdAnswer, medianFinder.findMedian(), stdAnswer);

        medianFinder = new MedianFinder();
        medianFinder.addNum(-1);
        stdAnswer = -1.0;
        medianFinder.findMedian();
        System.out.printf("%b %s %s\n", medianFinder.findMedian() == stdAnswer, medianFinder.findMedian(), stdAnswer);
        medianFinder.addNum(-2);
        stdAnswer = -1.5;
        medianFinder.findMedian();
        System.out.printf("%b %s %s\n", medianFinder.findMedian() == stdAnswer, medianFinder.findMedian(), stdAnswer);
        medianFinder.addNum(-3);
        stdAnswer = -2.0;
        medianFinder.findMedian();
        System.out.printf("%b %s %s\n", medianFinder.findMedian() == stdAnswer, medianFinder.findMedian(), stdAnswer);
        medianFinder.addNum(-4);
        stdAnswer = -2.5;
        medianFinder.findMedian();
        System.out.printf("%b %s %s\n", medianFinder.findMedian() == stdAnswer, medianFinder.findMedian(), stdAnswer);
        medianFinder.addNum(-5);
        stdAnswer = -3.0;
        medianFinder.findMedian();
        System.out.printf("%b %s %s\n", medianFinder.findMedian() == stdAnswer, medianFinder.findMedian(), stdAnswer);
    }
}