/***************************************************************************************************
 * Copyright: washing
 * FileName: 0944.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-5-12 11:23:55
***************************************************************************************************/

int minDeletionSize(char ** strs, int strsSize){
    int ret = 0;
    int n = strlen(strs[0]);
    char ** l = (char **)malloc(sizeof(char *) * n);
    for (int i=0; i<n; i++) l[i] = malloc(sizeof(char) * strsSize);
    for (int i=0; i<n; i++) {
        for (int j=0; j<strsSize; j++) {
            l[i][j] = strs[j][i];
            if (j > 0 && l[i][j-1] > l[i][j]) {
                ret += 1;
                break;
            }
        }
    }
    for (int i=0; i<n; i++) {
        free(l[i]);
    }
    free(l);
    return ret;
}
