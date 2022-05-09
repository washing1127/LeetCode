/***************************************************************************************************
 * Copyright: washing
 * FileName: 0942.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-5-9 11:20:42
***************************************************************************************************/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* diStringMatch(char * s, int* returnSize){
    int a = 0, b = strlen(s), idx=0;
    int * ret = (int *)malloc(sizeof(int) * (b+1));
    *returnSize = b + 1;
    for (int i = 0; i<strlen(s); i++) {
        if (s[i] == 'I') ret[idx++] = a++;
        else ret[idx++] = b--;
    }
    ret[idx] = a;
    return ret;
}
