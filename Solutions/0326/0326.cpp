class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n<1) return false;
        while(n>1){
            cout << n;
            if (n % 3 != 0) return false;
            n /= 3;
        }return true;
    }
};
