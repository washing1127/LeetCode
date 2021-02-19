/**
 * @Author: washing
 * @DateTime: 2021/02/19 17:11
 * @File: 1004.java
 * @Desc: 
 **/
class Solution {
    public int longestOnes(int[] A, int K) {
        int count = 0;
        int left = 0;

        for (int i : A) {
            if (i==0) count++;
            if (count>K) {
                if (A[left]==0) count--;
                left++;
            }
        }
        return A.length - left;
    }
}