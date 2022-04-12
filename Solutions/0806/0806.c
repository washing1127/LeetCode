/***************************************************************************************************
 * Copyright: washing
 * FileName: 0806.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-4-12 10:31:58
***************************************************************************************************/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numberOfLines(int* widths, int widthsSize, char * s, int* returnSize){
    int * ret = malloc(sizeof(int) * 2);
    ret[0] = 1;
    ret[1] = 0;
    while (*s) {
        if (ret[1] + widths[*s-'a'] > 100){
            ret[1] = widths[*s-'a'];
            ret[0]++;
        }else{
            ret[1] += widths[*s-'a'];
        }
        s++;
    }
    *returnSize=2;
    return ret;
}
