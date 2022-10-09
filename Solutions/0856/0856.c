/***************************************************************************************************
 * Copyright: washing
 * FileName: 0856.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-10-9 16:17:45
***************************************************************************************************/


int scoreOfParentheses(char * s){
    int * l = (int *)malloc(sizeof(int) * strlen(s));
    int idx = 0, i = 0;
    for (; i<strlen(s); i++) l[i] = -1;
    i = 0;
    for (;i<strlen(s);i++) {
        if (s[i] == '(') l[idx++] = 0;
        else {
            if (l[idx-1] == 0) l[idx-1] = 1;
            else {
                int sum = 0;
                for (; idx>0;) {
                    idx--;
                    if (l[idx] == 0) break;
                    sum += l[idx];
                }
                l[idx++] = sum*2;
            }
        }
    }
    int ret = 0;
    for (int k=0; k<idx; k++) ret += l[k];
    return ret;
}
