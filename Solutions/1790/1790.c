/***************************************************************************************************
 * Copyright: washing
 * FileName: 1790.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-10-11 16:01:16
***************************************************************************************************/


bool areAlmostEqual(char * s1, char * s2){
    int flag = 0;
    char a = '1', b = '1';
    for (int i=0; i<strlen(s1); i++) {
        if (s1[i] != s2[i]) {
            if (flag == 0) {
                a = s1[i];
                b = s2[i];
                flag++;
            } else if (flag == 1) {
                if (s2[i] == a && s1[i] == b) flag++;
                else return false;
            } else return false;
        }
    }
    return flag == 0 || flag == 2;
}
