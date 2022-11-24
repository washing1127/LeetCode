/***************************************************************************************************
 * Copyright: washing
 * FileName: 0795.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-11-24 11:43:01
***************************************************************************************************/

int numSubarrayBoundedMax(int* nums, int numsSize, int left, int right){
    int res=0,l=-1,lst=0;
    for (int i=0;i<numsSize;i++) {
        if (nums[i]>right) {
            l = i;
            lst=0;
        } else if (nums[i]>=left) {
            lst = i-l;
        }
        res += lst;
    }
    return res;
}
