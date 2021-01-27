// Author: washing
// DateTime: 2021/1/27 10:33
// File: 0171.c
// Desc: 

int titleToNumber(char * s){
    int n=0;
    int idx = 0;
    while (idx < strlen(s)){
        n = n*26 + ((int)s[idx] - 64);
        idx++;
    }
    return n;
}