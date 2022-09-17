/***************************************************************************************************
 * Copyright: washing
 * FileName: 1624.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-9-17 22:12:57
***************************************************************************************************/


int maxLengthBetweenEqualCharacters(char * s){
    int n = strlen(s);
    int ret = -1;
    for (int i=0; i<n; i++) {
        for (int j=n-1; j>i; j--) {
            if (s[i] == s[j] && ret < j-i-1) ret = j-i-1;
        }
    }
    return ret;
}
