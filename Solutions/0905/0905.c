/***************************************************************************************************
 * Copyright: washing
 * FileName: 0905.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-4-28 11:51:57
***************************************************************************************************/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortArrayByParity(int* nums, int numsSize, int* returnSize){
    int r = numsSize - 1;
    for (int i = 0; i < numsSize && i < r; i++) {
        while (nums[i] % 2 == 1 && i < r) {
            int temp = nums[r];
            nums[r--] = nums[i];
            nums[i] = temp;
        }
    }
    *returnSize = numsSize;
    return nums;
}
