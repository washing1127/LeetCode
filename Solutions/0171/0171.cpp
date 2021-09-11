// Author: washing
// DateTime: 2021/1/27 13:36
// File: 0171.cpp
// Desc: 

class Solution {
public:
    int titleToNumber(string s) {
        int n;
        int num = 0;
        for (auto &c : s){
            n = (int)c;
            num = num * 26 + (n-64);
        }

        return num;
    }
};