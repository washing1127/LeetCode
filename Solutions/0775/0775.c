/***************************************************************************************************
 * Copyright: washing
 * FileName: 0775.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-11-16 10:39:29
***************************************************************************************************/

bool isIdealPermutation(int* nums, int numsSize){
    if (numsSize == 1) return true;
    int mi = 0;
    if (nums[0] == 0 || nums[1] == 0) {
        mi++;
        if (nums[0] == 1 || nums[1] == 1) mi++;
    }
    for (int idx=0; idx < numsSize; idx++) {
        if (nums[idx] > mi) return false;
        while (1) {
            if (nums[idx] == mi) mi++;
            else if (idx+1 < numsSize) {
                if (nums[idx+1] == mi) mi++;
                else if (idx+2 < numsSize && nums[idx+2] == mi) mi++;
                else break;
            }
            else break;
        }
    }
    return true;
}
