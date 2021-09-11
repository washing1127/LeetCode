/**
 * @Author: washing
 * @DateTime: 2021/02/5 12:06
 * @File: 1208.java
 * @Desc: 
 **/
class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int l = 0;
        int r = 0;
        int totalCost = 0;
        while (r < s.length()){
            totalCost += Math.abs(s.charAt(r)-t.charAt(r));
            if (totalCost > maxCost){
                totalCost -= Math.abs(s.charAt(l)-t.charAt(l));
                l++;
            }
            r++;
        }
        return r-l;
    }
}