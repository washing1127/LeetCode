/***************************************************************************************************
 * Copyright: washing
 * FileName: 1662.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-11-01 10:29:11
***************************************************************************************************/


bool arrayStringsAreEqual(char ** word1, int word1Size, char ** word2, int word2Size){
    int x1=0,d1=0,x2=0,d2=0;
    while (d1<word1Size && d2<word2Size) {
        if (word1[d1][x1] != word2[d2][x2]) return false;
        else {
            x1++;
            x2++;
            if (x1 == strlen(word1[d1])) {
                x1 = 0;
                d1++;
            }
            if (x2 == strlen(word2[d2])) {
                x2 = 0;
                d2++;
            }
        }
    }
    return d1==word1Size && d2==word2Size;
}
