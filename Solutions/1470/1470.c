/***************************************************************************************************
 * Copyright: washing
 * FileName: 1470.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-8-29 10:11:06
***************************************************************************************************/




/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shuffle(int* nums, int numsSize, int n, int* returnSize){
    int *ret = (int *)malloc(sizeof(int) * numsSize);
    int idx = 0;
    for (int i=0; i<n; i++) {
        ret[idx++] = nums[i];
        ret[idx++] = nums[i+n];
    }
    *returnSize = numsSize;
    return ret;
}
