/***************************************************************************************************
 * Copyright: washing
 * FileName: 1785.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-12-16 10:14:49
***************************************************************************************************/

int minElements(int* nums, int numsSize, int limit, int goal){
    long sm = 0;
    for (int i=0; i<numsSize; i++) sm += nums[i];
    long left = goal - sm;
    if (left < 0) left = 0 - left;
    int ret = left / limit;
    if (left % limit) ret++;
    return ret;
}
