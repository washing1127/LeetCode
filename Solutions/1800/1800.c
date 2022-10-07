/***************************************************************************************************
 * Copyright: washing
 * FileName: 1800.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-10-7 18:42:36
***************************************************************************************************/


int maxAscendingSum(int* nums, int numsSize){
    int temp=nums[0], ret=nums[0];
    for (int i=1; i<numsSize; i++) {
        if (nums[i] > nums[i-1]) temp += nums[i];
        else temp = nums[i];
        ret = fmax(temp, ret);
    }
    return ret;
}
