/***************************************************************************************************
 * Copyright: washing
 * FileName: 1464.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-08-26 08:25:27
***************************************************************************************************/


int maxProduct(int* nums, int numsSize){
    int a=0, b=0;
    for (int i=0; i<numsSize; i++) {
        if (nums[i] >= a) {
            if (nums[i] >= b) {
                a = b;
                b = nums[i];
            }
            else a = nums[i];
        }
    }
    return (a-1) * (b-1);
}
