/***************************************************************************************************
 * Copyright: washing
 * FileName: 0769.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-10-13 10:54:27
***************************************************************************************************/

int maxChunksToSorted(int* arr, int arrSize){
    int ret = 0;
    int mi = arrSize;
    int ma = 0;
    int l = 0;
    for (int idx=0; idx<arrSize; idx++) {
        int i = arr[idx];
        ma = i > ma ? i : ma;
        mi = i < mi ? i : mi;
        if (mi == l && ma == idx) {
            ret++;
            l = idx+1;
            mi = arrSize;
        }
    }
    return ret;
}
