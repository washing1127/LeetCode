/***************************************************************************************************
 * Copyright: washing
 * FileName: √Ê ‘Ã‚01.02.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-9-27 11:29:58
***************************************************************************************************/

int cmp(const void* _a, const void* _b) {
    char a = *(char*)_a, b = *(char*)_b;
    return a - b;
}

bool CheckPermutation(char* s1, char* s2){
    if (strlen(s1) != strlen(s2)) return false;
    qsort(s1, strlen(s1), sizeof(char), cmp);
    qsort(s2, strlen(s2), sizeof(char), cmp);
    return strcmp(s1, s2) == 0;
}
