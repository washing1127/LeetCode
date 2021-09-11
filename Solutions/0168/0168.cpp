// Author: washing
// DateTime: 2021/6/29 15:37
// File: 0168.cpp
// Desc: 

class Solution {
public:
    string convertToTitle(int columnNumber) {
        string s = "";
        int r;
        while (columnNumber != 0){
            r = columnNumber % 26;
            columnNumber = columnNumber / 26;
            if (r == 0){
                r = 26;
                columnNumber--;
            }
            r += 64;
            s = (char)r + s;
        }
        return s;
    }
};
