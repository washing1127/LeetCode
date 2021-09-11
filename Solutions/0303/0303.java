/**
 * @Author: washing
 * @DateTime: 2021/3/1 8:45
 * @File: 0303.java
 * @Desc: 
 **/
class NumArray {
    int[] list;
    public NumArray(int[] nums) {
        this.list = nums;
    }
    
    public int sumRange(int i, int j) {
        int ans = 0;
        for (int idx=i; idx<j+1 && idx<this.list.length; idx++){
            ans += this.list[idx];
        }
        return ans;
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(i,j);
 */