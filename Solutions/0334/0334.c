bool increasingTriplet(int* nums, int numsSize){
    if (numsSize < 3) return false;
    int zx = nums[0], ex = INT_MAX;
    for (int i=1; i<numsSize; i++){
        int num = nums[i];
        if (num < zx) zx = num;
        else if (num > zx){
            if (num > ex) return true;
            ex = num;
        }
    }
    return false;
}
