/***************************************************************************************************
 * Copyright: washing
 * FileName: 0908.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-4-30 19:18:54
***************************************************************************************************/

int smallestRangeI(int* nums, int numsSize, int k){
    int max = 0;
    int min = 10000;
    for (int i = 0; i < numsSize; i++){
        max = fmax(max, nums[i]);
        min = fmin(min, nums[i]);
    }
    return fmax(max - min - k*2, 0);
}
