class Solution {
public:
    int balancedStringSplit(string s) {
        int r=0;
        int l=0;
        int ret = 0;
        int n = std::end(s) - std::begin(s);
        for (int i=0; i<n; i++){
            if (s[i] == 'R') r++;
            else l++;
            if (r == l) ret++;
        }
        return ret;
    }
};
