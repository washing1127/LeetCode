// Author: washing
// DateTime: 2021/9/3 18:50
// File: 面试题17.14.cpp
// Desc: 


class Solution {
public:
    vector<int> smallestK(vector<int>& arr, int k) {
        vector<int> vec(k, 0);
        sort(arr.begin(), arr.end());
        for (int i=0; i < k; i++) vec[i] = arr[i];
        return vec;
    }
};