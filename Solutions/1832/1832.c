/***************************************************************************************************
 * Copyright: washing
 * FileName: 1832.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-12-13 11:12:16
***************************************************************************************************/

bool checkIfPangram(char * sentence){
    int * li[26];
    for (int i=0; i<26; i++) {
        li[i] = 0;
    }
    for (int i=0;i<strlen(sentence);i++) {
        char c = sentence[i];
        li[c-97]++;
    }
    bool ret = true;
    for (int i=0; i<26; i++) {
        if (li[i] == 0) ret = false;
    }
    return ret;
}
