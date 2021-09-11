/**
 * @Author: washing
 * @DateTime: 2021/01/21 14:01
 * @File: 0007.java
 * @Desc: 
 **/

class Solution {
    public int reverse(int x) {
        
        long n = 0;
        while(x != 0) {
            n = n * 10 + x % 10;
            x = x / 10;
        }
        if (n < -2147483648 || n > 2147483647){
            return 0;
        } else {
            return (int)n;
        }
    }
}