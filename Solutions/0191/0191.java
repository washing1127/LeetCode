/**
 * @Author: washing
 * @DateTime: 2021/01/23 23:07
 * @File: 0191.java
 * @Desc: 
 **/

public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int count = 0;
        while(n!=0) {
            n&=(n-1);
            count++;
        }
        return count;
    }
}