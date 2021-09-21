class Solution {
public:
    int lengthOfLastWord(string s) {
        int n = std::end(s)-std::begin(s);
        int ret = 0;
        for (int i=n-1; i>=0; i--){
            if (ret == 0 && s[i] == ' ') continue;
            if (s[i] != ' ') ret++;
            if (s[i] == ' ') break;
        }
        return ret;
    }
};
