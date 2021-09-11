// Author: washing
// DateTime: 2021/4/20 10:08
// File: 0028.java
// Desc: 

class Solution {
    public int strStr(String haystack, String needle) {
        int l = needle.length();
        if (needle.equals("")) return 0;
        for(int i=0; i<=haystack.length()-l; i++){
            if(haystack.substring(i, i+l).equals(needle)) return i;
        }
        return -1;
    }
}