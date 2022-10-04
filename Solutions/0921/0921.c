/***************************************************************************************************
 * Copyright: washing
 * FileName: 0921.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-10-4 11:01:36
***************************************************************************************************/

int minAddToMakeValid(char * s){
    char * l = (char *)malloc(sizeof(char) * strlen(s));
    int idx = 0;
    for (int i=0; i<strlen(s); i++) {
        if (s[i] == ')') {
            if (idx>0 && l[idx-1] == '(') {
                idx--;
                l[idx] = '-';
                continue;
            }
        }
        l[idx++] = s[i];
    }
    return idx;
}
