/***************************************************************************************************
 * Copyright: washing
 * FileName: 0396.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-4-22 12:05:05
***************************************************************************************************/

int maxRotateFunction(int* nums, int numsSize){
    int sm = 0, ret = 0;
    for (int i = 0; i < numsSize; i++) {
        sm += nums[i];
        ret += nums[i] * i;
    }
    int f0 = ret;
    for (int idx=numsSize-1; idx>=0; idx--) {
        f0 = f0 + sm - nums[idx] * numsSize;
        ret = fmax(f0, ret);
    }
    return ret;
}
