/***************************************************************************************************
 * Copyright: washing
 * FileName: 1704.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-11-11 11:02:30
***************************************************************************************************/


bool halvesAreAlike(char * s){
    int i=0,j=strlen(s)-1;
    int ct1 = 0, ct2 = 0;
    for (;i<j;i++,j--) {
        char si = s[i];
        char sj = s[j];
        if ((si-'a')==0 || (si-'e')==0 || (si-'i')==0 || (si-'o')==0 || (si-'u')==0 || (si-'A')==0 || (si-'E')==0 || (si-'I')==0 || (si-'O')==0 || (si-'U')==0) ct1++;
        if ((sj-'a')==0 || (sj-'e')==0 || (sj-'i')==0 || (sj-'o')==0 || (sj-'u')==0 || (sj-'A')==0 || (sj-'E')==0 || (sj-'I')==0 || (sj-'O')==0 || (sj-'U')==0) ct2++;
    }
    return ct1==ct2;
}
