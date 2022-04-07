/***************************************************************************************************
 * Copyright: washing
 * FileName: 0796.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-4-7 09:59
***************************************************************************************************/

bool rotateString(char * s, char * goal){
    int i, len=strlen(s);
    if (strcmp(s, goal) == 0) return true;
    for (i=0; i<len; i++){
        char a = s[0];
        for (int j=1; j<len; j++){
            s[j-1] = s[j];
        }
        s[len-1] = a;
        if (strcmp(s, goal) == 0) return true;
    }
    return false;
}
