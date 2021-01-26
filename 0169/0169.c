// Author: washing
// DateTime: 2021/1/26 18:50
// File: 0169.c
// Desc: 

int majorityElement(int* nums, int numsSize){
    int a = 0;
    int c = 0;
    for (int i=0; i<numsSize; i++){
        if (c==0){
            a = nums[i];
            c++;
        }else if (a==nums[i]){
            c++;
        }else{
            c--;
        }
    }
    return a;
}