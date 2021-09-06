class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l=0;
        int r = std::end(nums) - std::begin(nums) - 1;
        while(l<r){
            int m = (l+r)/2;
            int num = nums[m];
            if (num < target) l = m+1;
            else if (num > target) r = m;
            else return m;
        }
        if (nums[r] == target) return r;
        else return -1;
    }
};
