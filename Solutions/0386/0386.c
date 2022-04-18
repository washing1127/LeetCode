/***************************************************************************************************
 * Copyright: washing
 * FileName: 0386.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-4-18 12:42:23
***************************************************************************************************/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* lexicalOrder(int n, int* returnSize){
    int *ans = (int *)malloc(sizeof(int) * n);
    int num = 1;
    for(int i=0; i<n; i++){
        ans[i] = num;
        if (num * 10 <= n) num *= 10;
        else {
            while (num % 10 == 9 || num >= n) num /= 10;
            num += 1;
        }
    }
    *returnSize = n;
    return ans;
}
