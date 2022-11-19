/***************************************************************************************************
 * Copyright: washing
 * FileName: 1732.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-11-19 15:11:49
***************************************************************************************************/

int largestAltitude(int* gain, int gainSize){
    int ret=fmax(0, gain[0]);
    for (int i=1; i<gainSize; i++) {
        gain[i] += gain[i-1];
        ret = fmax(ret, gain[i]);
    }
    return ret;
}
