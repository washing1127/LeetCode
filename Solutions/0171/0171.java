// Author: washing
// DateTime: 2021/1/27 10:34
// File: 0171.java
// Desc: 

class Solution {
    public int titleToNumber(String s) {
        char i;
        int n=0;
        for (int idx=0; idx < s.length(); idx++){
            i = s.charAt(idx);
            n = n*26+(int)i-64;
        }
        return n;
    }
}