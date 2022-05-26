/***************************************************************************************************
 * Copyright: washing
 * FileName: 0699.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-5-26 16:55:12
***************************************************************************************************/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* fallingSquares(int** positions, int positionsSize, int* positionsColSize, int* returnSize){
    int * ret = (int *)malloc(sizeof(int) * positionsSize);
    int * l = (int *)malloc(sizeof(int) * positionsSize * 3);
    int lidx = 0;
    int ma = 0;
    for (int i=0; i<positionsSize; i++) {
        int a = positions[i][0];
        int b = positions[i][1];
        l[lidx*3] = a;
        l[lidx*3+1] = a+b;
        l[lidx*3+2] = b;
        for (int j=0; j<lidx; j++) {
            int x1=l[j*3], x2=l[j*3+1], y=l[j*3+2];
            if (x1<=a&&a<x2 || x1<a+b&&a+b<=2 || a<=x1&&x1<a+b || a<x2&&x2<=a+b) {
                l[lidx*3+2] = fmax(l[lidx*3+2], y+b);
            }
        }
        ma = fmax(l[lidx*3+2], ma);
        ret[lidx++] = ma;
    }

    *returnSize = positionsSize;
    return ret;
}
