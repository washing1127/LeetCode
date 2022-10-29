/***************************************************************************************************
 * Copyright: washing
 * FileName: 1773.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-10-29 10:24:33
***************************************************************************************************/

int countMatches(char *** items, int itemsSize, int* itemsColSize, char * ruleKey, char * ruleValue){
    int ret = 0;
    int idx;
    char s1[] = "type";
    char s2[] = "color";
    if (strcmp(ruleKey, s1) == 0) idx = 0;
    else if (strcmp(ruleKey, s2) == 0) idx = 1;
    else idx = 2;
    for (int j=0; j<itemsSize; j++) {
        if (strcmp(items[j][idx], ruleValue) == 0) ret++;
    }
    return ret;
}
