/**
 * @Author: washing
 * @DateTime: 2021/01/25 17:38
 * @File: 0168.java
 * @Desc: 
 **/
class Solution {
    public String convertToTitle(int n) {
        String s = "";
        int r;
        while (n != 0) {
            r = n % 26;
            n = n / 26;
            if (r == 0) {
                r = 26;
                n--;
            }
            r += 64;
            s = (char) r + s;
        }
        return s;
    }
}