/**
 * @Author: washing
 * @DateTime: 2021/02/16 11:34
 * @File: 0561.java
 * @Desc: 
 **/

class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int count = 0;
        for (int i=0; i<nums.length; i+=2){
            count += nums[i];
        }
        return count;
    }
}