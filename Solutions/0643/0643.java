/**
 * @Author: washing
 * @DateTime: 2021/02/04 17:48
 * @File: 0643.java
 * @Desc: 
 **/
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int biggest = 0;
        for (int i=0; i<k; i++){
            biggest += nums[i];
        }
        int num = biggest;
        for (int i=1; i<nums.length-k+1; i++){
            num = num - nums[i-1] + nums[i+k-1];
            biggest = num > biggest ? num : biggest;
        }
        return biggest/(double)k;
    }
}