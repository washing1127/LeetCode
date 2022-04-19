/***************************************************************************************************
 * Copyright: washing
 * FileName: 0821.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-4-21 13:41:50
***************************************************************************************************/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shortestToChar(char * s, char c, int* returnSize){
    int * ret = (int *)malloc(sizeof(int) * strlen(s));
    int n = strlen(s);
    for (int i=0; i<n; i++) ret[i] = n;
    for (int i=0; i<n; i++){
        if (s[i] == c) {
            ret[i] = 0;
            for (int l=i-1; l>=0; l--) {
                if (ret[l] > i-l) ret[l] = i-l;
                else break;
            }
            for (int r=i+1; r<n; r++){
                if (ret[r] > r-i) ret[r] = r-i;
                else break;
            }
        }
    }
    *returnSize = n;
    return ret;
}
