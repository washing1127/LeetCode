// Author: washing
// DateTime: 2021/1/28 15:28
// File: Offer64.java
// Desc: 

class Solution {
    public int sumNums(int n) {
        return n & (n+sumNums(n-1));
    }
}