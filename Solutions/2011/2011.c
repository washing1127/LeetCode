/***************************************************************************************************
 * Copyright: washing
 * FileName: 2011.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-12-23 10:02:24
***************************************************************************************************/

int finalValueAfterOperations(char ** operations, int operationsSize){
    int ret = 0;
    for (int i=0; i<operationsSize; i++){
        if (operations[i][1] == '+') ret++;
        else ret--;
    }
    return ret;
}
