/***************************************************************************************************
 * Copyright: washing
 * FileName: 1417.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-8-12 18:20:32
***************************************************************************************************/



char * reformat(char * s){
    char * s1 = (char *)malloc(sizeof(char) * strlen(s));
    char * s2 = (char *)malloc(sizeof(char) * strlen(s));
    int id1=0, id2=0;
    for (int i=0; i<strlen(s); i++){
        if (s[i]<='z' && s[i]>='a') {
            s1[id1++] = s[i];
        } else {
            s2[id2++] = s[i];
        }
    }
    char * ret = (char *)malloc(sizeof(char) * (strlen(s) + 1));
    int id = 0;
    if (id1 - id2 > 1 || id2 - id1 > 1) ret[id] = '\0';
    else if (id1 == id2) {
        for (;id<id1;id++) {
            ret[id*2] = s1[id];
            ret[id*2+1] = s2[id];
        }
        ret[id*2] = '\0';
    } else if (id1 < id2) {
        for (;id<id1;id++) {
            ret[id*2] = s2[id];
            ret[id*2+1] = s1[id];
        }
        ret[id*2] = s2[id];
        ret [id*2+1] = '\0';
    } else {
        for (;id<id2;id++) {
            ret[id*2] = s1[id];
            ret[id*2+1] = s2[id];
        }
        ret[id*2] = s1[id];
        ret[id*2+1] = '\0';
    }
    return ret;
}
