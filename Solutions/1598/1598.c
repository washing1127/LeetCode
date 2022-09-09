/***************************************************************************************************
 * Copyright: washing
 * FileName: 1598.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-9-9 11:13:36
***************************************************************************************************/

int minOperations(char ** logs, int logsSize){
    int ret = 0;
    for (int i=0; i<logsSize; i++) {
        if (strcmp(logs[i], "../") == 0) {
            if (ret > 0) ret--;
        } else if (strcmp(logs[i], "./") != 0) ret++;
    }
    return ret;
}
