# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
 

# Example:

# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

class stackNode {
    public int data;
    public int min;
    public stackNode next;
    public stackNode (){
        data = 0;
        min = 0;
        next = null;
    }
    public stackNode (int d){
        data = d;
        min = d;
        next = null;
    }
    public stackNode (int d, int m, stackNode n ){
        min = m;
        data = d;
        next = n;
    }
}

class MinStack {
    private stackNode top;    
    /** initialize your data structure here. */
    public MinStack() {
        top = null;
    }
    
    public void push(int x) {
        if (top == null){
            top =  new stackNode(x);
        }else{
            int min = top.min;
            if (x < top.min){
                min = x;
            }
            stackNode n = new stackNode(x, min, top);
            top = n;
        }
    }
    
    public void pop() {
        top = top.next;
    }
    
    public int top() {
        return top.data;
    }
    
    public int getMin() {
        return top.min;
    }
}