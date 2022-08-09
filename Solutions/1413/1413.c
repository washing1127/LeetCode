/***************************************************************************************************
 * Copyright: washing
 * FileName: 1413.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-8-10 10:55:54
***************************************************************************************************/


int minStartValue(int* nums, int numsSize){
    int min = nums[0];
    for (int i=1; i<numsSize; i++){
        nums[i] += nums[i-1];
        if (nums[i] < min) min = nums[i];
    }
    return min < 0 ? -min+1 : 1;
}
