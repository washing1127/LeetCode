class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.end() - digits.begin();
        int p = 1;
        for (int i=n-1; i>=0; i--){
            if (digits[i] == 9){
                digits[i] = 0;
                p = 1;
            }else {
                digits[i]++;
                p = 0;
            }
            if (p == 0) break;
        }
        if (p) digits.insert(digits.begin(), 1);
        return digits;
    }
};
