class Solution {
public:
    int fib(int n) {
        if (n == 0) return 0;
        if (n <= 2) return 1;
        long long a = 1;
        long long b = 1;
        for (int i=2; i<n; i++){
            b += a;
            a = b - a;
            b %= 1000000007;
            a %= 1000000007;
        }
        return b;
    }
};
