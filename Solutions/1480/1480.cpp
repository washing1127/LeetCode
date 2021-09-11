// Author: washing
// DateTime: 2021/8/28 18:50
// File: 1480.cpp
// Desc: 


class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int n = std::end(nums)-std::begin(nums);
        for (int i=1; i<n; i++){
            nums[i] = nums[i]+nums[i-1];
        }
        return nums;
    }
};