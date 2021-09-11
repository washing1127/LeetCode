// Author: washing
// DateTime: 2021/1/26 18:51
// File: 0169.cs
// Desc: 


public class Solution {
    public int MajorityElement(int[] nums) {
        int a=0;
        int c=0;
        int n;
        for (int i=0; i<nums.Length;i++){
            n = nums[i];
            if (c==0){
                a = n;
                c++;
            }else if (a==n){
                c++;
            }else{
                c--;
            }
        }
        return a;
    }
}