char * convert(char * s, int numRows){
    int n = strlen(s), r = numRows;
    if (r == 1 || r >= n) {
        return s;
    }
    int t = r * 2 - 2;
    char * ans = (char *)malloc(sizeof(char) * (n + 1));
    int pos = 0;
    for (int i = 0; i < r; ++i) { // 枚举矩阵的行
        for (int j = 0; j + i < n; j += t) { // 枚举每个周期的起始下标
            ans[pos++] = s[j + i]; // 当前周期的第一个字符
            if (0 < i && i < r - 1 && j + t - i < n) {
                ans[pos++] = s[j + t - i]; // 当前周期的第二个字符
            }
        }
    }
    ans[pos] = '\0';
    return ans;
}

