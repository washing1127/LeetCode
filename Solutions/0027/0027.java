// Author: washing
// DateTime: 2021/4/19 10:10
// File: 0027.java
// Desc: 

class Solution {
    public int removeElement(int[] nums, int val) {
        int r = nums.length-1;
        int l = 0;
        while (l <= r){
            if (nums[r] == val) r--;
            else {
                if (nums[l] == val){
                    nums[l] = nums[r];
                    r--;
                }
                l++;
            }
        }
        return l;
    }
}