import java.util.*;

class MyStack {
    private Queue<Integer>[] q = new LinkedList[2];
    private int idx = 0;

    /**
     * Initialize your data structure here.
     */
    public MyStack() {
        q[0] = new LinkedList<>();
        q[1] = new LinkedList<>();
    }

    /**
     * Push element x onto stack.
     */
    public void push(int x) {
        q[idx].add(x);
        if (q[idx].size() > 1) q[1 - idx].add(q[idx].remove());
    }

    /**
     * Removes the element on top of the stack and returns that element.
     */
    public int pop() {
        int val = q[idx].remove();
        while (q[1 - idx].size() > 1) q[idx].add(q[1 - idx].remove());
        idx = 1 - idx;
        return val;
    }

    /**
     * Get the top element.
     */
    public int top() {
        return q[idx].element();
    }

    /**
     * Returns whether the stack is empty.
     */
    public boolean empty() {
        return q[idx].isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */

public class Main {
    public static void main(String[] args) {
        MyStack myStack = new MyStack();
        myStack.push(1);
        myStack.push(2);
        System.out.printf("%d %d\n", myStack.top(), 2);
        System.out.printf("%d %d\n", myStack.pop(), 2);
        System.out.printf("%b %b\n", myStack.empty(), false);
    }
}