/**
 * @Author: washing
 * @DateTime: 2021/03/6 22:34
 * @File: 0503.java
 * @Desc: 
 **/

class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int len = nums.length;
        int[] ret = new int[len];
        Deque<Integer> stk = new LinkedList<Integer>();
        Arrays.fill(ret, -1);

        for (int i=0; i<2*len-1; i++){
            int idx = i % len;
            while (!stk.isEmpty() && nums[stk.peek()] < nums[idx]){
                ret[stk.pop()] = nums[idx];
            }
            stk.push(idx);
        }
        return ret;
    }
}