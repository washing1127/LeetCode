/***************************************************************************************************
 * Copyright: washing
 * FileName: 1758.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-11-29 10:33:03
***************************************************************************************************/


int minOperations(char * s){
    int ret1=0, ret2=0;
    char ta='1', tb='0';
    for (int i=0;i<strlen(s);i++) {
        if (s[i] != ta) ret1++;
        if (s[i] != tb) ret2++;
        ta = ta == '1' ? '0' : '1';
        tb = tb == '1' ? '0' : '1';
    }
    return ret1 > ret2 ? ret2 : ret1;
}
