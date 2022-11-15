/***************************************************************************************************
 * Copyright: washing
 * FileName: 1710.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-11-15 10:05:52
***************************************************************************************************/


static inline int cmp(const void *pa, const void *pb) {
    return (*(int **)pb)[1] - (*(int **)pa)[1];
}

int maximumUnits(int** boxTypes, int boxTypesSize, int* boxTypesColSize, int truckSize){
    qsort(boxTypes, boxTypesSize, sizeof(int *), cmp);
    int ret = 0;
    int idx = 0;
    while (truckSize != 0 && idx < boxTypesSize) {
        int a = boxTypes[idx][0], b = boxTypes[idx][1];
        idx++;
        if (truckSize > a) {
            truckSize -= a;
            ret += a*b;
        } else {
            ret += truckSize*b;
            truckSize = 0;
        }
    }
    return ret;
}
