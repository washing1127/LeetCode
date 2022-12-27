/***************************************************************************************************
 * Copyright: washing
 * FileName: 2027.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-12-27 10:01:28
***************************************************************************************************/


int minimumMoves(char * s){
    int ret=0;
    for (int i=0; i<strlen(s); i++) {
        if (s[i] == 'X') {
            s[i] = 'O';
            if (i+1 < strlen(s)) s[i+1] = 'O';
            if (i+2 < strlen(s)) s[i+2] = 'O';
            ret++;
        }
    }
    return ret;
}
