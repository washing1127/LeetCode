/***************************************************************************************************
 * Copyright: washing
 * FileName: 1822.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-10-27 11:34:06
***************************************************************************************************/

int arraySign(int* nums, int numsSize){
    int ret = 1;
    for (int i=0; i<numsSize; i++) {
        if (nums[i] == 0) return 0;
        if (nums[i] < 0) ret *= -1;
    }
    return ret;
}
