// Author: washing
// DateTime: 2021/1/26 18:50
// File: 0169.cpp
// Desc: 


class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int a=0;
        int c=0;
        for (auto i : nums){
            if (c==0){
                a = i;
                c++;
            }else if (a==i){
                c++;
            }else {
                c--;
            }
        }
        return a;
    }
};