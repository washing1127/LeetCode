/**
 * @Author: washing
 * @DateTime: 2021/3/5 10:12
 * @File: 0232.java
 * @Desc: 
 **/
class MyQueue {

    Deque<Integer> inStack;
    Deque<Integer> outStack;

    /** Initialize your data structure here. */
    public MyQueue() {
        inStack = new LinkedList<Integer>();
        outStack = new LinkedList<Integer>();
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        inStack.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        if (outStack.isEmpty())
        {
            while (!inStack.isEmpty())
            {
                outStack.push(inStack.pop());
            }
        }
        return outStack.pop();
    }
    
    /** Get the front element. */
    public int peek() {
        if (outStack.isEmpty())
        {
            while (!inStack.isEmpty())
            {
                outStack.push(inStack.pop());
            }
        }
        return outStack.peek();
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return inStack.isEmpty() && outStack.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */