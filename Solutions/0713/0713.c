/***************************************************************************************************
 * Copyright: washing
 * FileName: 0713.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-5-5 20:09:46
***************************************************************************************************/

int numSubarrayProductLessThanK(int* nums, int numsSize, int k){
    int ret = 0;
    for (int i=0; i<numsSize; i++) {
        int ji = 1;
        for (int j=i; j<numsSize; j++) {
            ji *= nums[j];
            if (ji < k) ret++;
            else break;
        }
    }
    return ret;
}
