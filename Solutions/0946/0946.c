/***************************************************************************************************
 * Copyright: washing
 * FileName: 0946.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-8-31 11:52:57
***************************************************************************************************/


bool validateStackSequences(int* pushed, int pushedSize, int* popped, int poppedSize){
    int * temp = (int *)malloc(sizeof(int) * pushedSize);
    int pushidx=0, popidx=0, tempidx=0;
    while (popidx < poppedSize) {
        if (tempidx > 0 && temp[tempidx-1] == popped[popidx]) {
            tempidx--;
            popidx++;
        } else if (pushidx < pushedSize) {
            temp[tempidx++] = pushed[pushidx++];
        } else break;
    }
    return tempidx == 0 || (tempidx==1 && temp[0] == popped[popidx-1]);
}
