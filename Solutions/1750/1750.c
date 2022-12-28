/***************************************************************************************************
 * Copyright: washing
 * FileName: 1750.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-12-28 10:10:35
***************************************************************************************************/

int minimumLength(char * s){
    int n = strlen(s);
    int l = 0, r = n - 1;
    while (1) {
        if (l==r || s[l] != s[r]) break;
        char c = s[l];
        while (l < n && s[l] == c) l++;
        while (r > 0 && s[r] == c) r--;
        if (r < l) {
            return 0;
        }
    }
    return r-l+1;
}
