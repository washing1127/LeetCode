/***************************************************************************************************
 * Copyright: washing
 * FileName: 1475.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-9-1 10:37:18
***************************************************************************************************/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* finalPrices(int* prices, int pricesSize, int* returnSize){
    int * ret = (int *)malloc(sizeof(int *) * pricesSize);
    for (int idx1=0; idx1<pricesSize;idx1++){
        int i = prices[idx1];
        bool flag = true;
        for (int idx2=idx1+1; idx2<pricesSize; idx2++) {
            int j = prices[idx2];
            if (j <= i) {
                ret[idx1] = i-j;
                flag = false;
                break;
            }
        }
        if (flag) ret[idx1] = i;
    }
    *returnSize = pricesSize;
    return ret;
}
