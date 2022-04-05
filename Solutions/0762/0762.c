int countPrimeSetBits(int left, int right){
    int s[] = {2, 3, 5, 7, 11, 13, 17, 19, 23};
    int ret = 0;
    for (int x = left; x <= right; x++){
        bool flag = false;
        for (int idx = 0; idx < 9; idx++){
            if (s[idx] == __builtin_popcount(x)) flag = true;
        }
        if (flag) ret++;
    }
    return ret;
}
