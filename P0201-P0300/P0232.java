import java.util.Stack;

class MyQueue {
    Stack<Integer> stack1, stack2;

    /**
     * Initialize your data structure here.
     */
    public MyQueue() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }

    /**
     * Push element x to the back of queue.
     */
    public void push(int x) {
        stack2.push(x);
    }

    /**
     * Removes the element from in front of queue and returns that element.
     */
    public int pop() {
        if (stack1.empty()) {
            while (!stack2.empty()) stack1.push(stack2.pop());
        }
        return stack1.pop();
    }

    /**
     * Get the front element.
     */
    public int peek() {
        if (stack1.empty()) {
            while (!stack2.empty()) stack1.push(stack2.pop());
        }
        return stack1.peek();
    }

    /**
     * Returns whether the queue is empty.
     */
    public boolean empty() {
        return stack1.empty() && stack2.empty();
    }
}

public class Main {
    public static void main(String[] args) {
        MyQueue myQueue = new MyQueue();
        myQueue.push(1);
        myQueue.push(2);
        System.out.printf("%d %d\n", myQueue.peek(), 1);
        System.out.printf("%d %d\n", myQueue.pop(), 1);
        System.out.printf("%b %b\n", myQueue.empty(), false);
    }
}