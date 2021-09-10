class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        int n = std::end(chalk)-std::begin(chalk);
        long s = 0;
        for(int i=0;i<n;i++) s+=chalk[i];
        k %= s;
        int idx = 0;
        while (true){
            k -= chalk[idx];
            if (k<0) return idx;
            idx ++;
            if (idx==n) idx=0;
        }
    }
};
