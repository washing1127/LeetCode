// Author: washing
// DateTime: 2021/1/26 18:52
// File: 0169.java
// Desc: 

class Solution {
    public int majorityElement(int[] nums) {
        int a = nums[0];
        int c = 1;
        int i;
        for (int n=1; n<nums.length;n++){
            i = nums[n];
            if (c == 0){
                a = i;
                c++;
            }else if (i == a){
                c++;
            }else{
                c--;
            }
        }
        return a;
    }
}