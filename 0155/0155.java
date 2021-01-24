/**
 * @Author: washing
 * @DateTime: 2021/01/24 20:22
 * @File: 0155.java
 * @Desc: 
 **/
class MinStack {

    /** initialize your data structure here. */
    // private List ret;
    private ArrayList ret = new ArrayList();
    public MinStack() {
    }
    
    public void push(int x) {
        this.ret.add(0, x);
    }
    
    public void pop() {
        this.ret.remove(0);
    }
    
    public int top() {
        return (int)this.ret.get(0);
    }
    
    public int getMin() {
        int min = (int)this.ret.get(0);
        for (int i=0; i<this.ret.size(); i++){
            if (min > (int)this.ret.get(i)){
                min = (int)this.ret.get(i);
            }
        }
        return min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */