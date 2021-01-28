// Author: washing
// DateTime: 2021/1/28 15:28
// File: Offer64.cpp
// Desc: 

class Solution {
public:
    int sumNums(int n) {
        return ((int)pow(n, 2) + n) >> 1;
        n && (n += sumNums(n - 1));
        return n;
    }
};