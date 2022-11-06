/***************************************************************************************************
 * Copyright: washing
 * FileName: 1678.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-11-07 14:39:04
***************************************************************************************************/


char * interpret(char * command){
    int n=0;
    for (int i=0; i<strlen(command); i++){
        if (command[i]=='G' || command[i]=='(' || command[i] == 'a') n++;
    }
    char * ret = (char *)malloc(sizeof(char)*(n+1));
    int i2=0;
    for (int idx=0; idx<strlen(command); idx++){
        if (command[idx] == 'G') ret[i2++] = 'G';
        else if (command[idx] == '(' && command[idx+1] == ')') ret[i2++] = 'o';
        else if (command[idx] == 'a') {
            ret[i2++] = 'a';
            ret[i2++] = 'l';
        }
    }
    ret[n] = '\0';
    return ret;
}
