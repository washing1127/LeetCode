class Solution {
public:
    int minSteps(int n) {
        int ret = 0;
        while (n > 1){
            for (int i=2; i<=n;i++){
                int ys = n % i ;
                if (ys == 0){
                    ret += i;
                    n = n / i;
                    break;
                }
            }
        }
        return ret;
    }
};
