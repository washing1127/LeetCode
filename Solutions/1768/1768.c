/***************************************************************************************************
 * Copyright: washing
 * FileName: 1768.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-10-23 17:39:46
***************************************************************************************************/


char * mergeAlternately(char * word1, char * word2){
    int n1 = strlen(word1);
    int n2 = strlen(word2);
    char * ret = (char *)malloc(sizeof(char) * (n1+n2+1));
    // char * ret = (char *)malloc(sizeof(char) * (strlen(word1) + strlen(word2) + 1));
    int i = 0;
    int j = 0;
    while (j < strlen(word1) || j < strlen(word2)) {
        if (j < strlen(word1)) {
            ret[i++] = word1[j];
        }
        if (j < strlen(word2)) {
            ret[i++] = word2[j];
        }
        j++;
    }
    ret[i] = '\0';
    return ret;
}
