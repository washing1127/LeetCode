class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int l=0, r=nums.size()-1;
        while (l<r){
            int m = (l+r)/2;
            nums[m] < nums[m+1]? l=m+1 : r=m;
        }
        return l;
    }
};
