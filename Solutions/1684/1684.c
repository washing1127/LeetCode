/***************************************************************************************************
 * Copyright: washing
 * FileName: 1684.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-11-08 10:10:20
***************************************************************************************************/

int countConsistentStrings(char * allowed, char ** words, int wordsSize){
    int ret = 0;
    for (int i=0; i<wordsSize; i++) {
        bool flag1 = true;
        for (int j=0; j<strlen(words[i]); j++) {
            bool flag2 = false;
            for (int k=0; k<strlen(allowed); k++) {
                if (allowed[k] == words[i][j]) {
                    flag2 = true;
                    break;
                }
            }
            if (!flag2) {
                flag1 = false;
                break;
            }
        }
        if (flag1) ret++;
    }
    return ret;
}
