/***************************************************************************************************
 * Copyright: washing
 * FileName: 1422.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-8-15 10:43:01
***************************************************************************************************/


int maxScore(char * s){
    int z, y = 0;
    z = s[0] == '0' ? 1 : 0;
    for (int i=1; i<strlen(s); i++) {
        if (s[i] == '1') y++;
    }
    int max = z + y;
    for (int i=1; i<strlen(s)-1; i++) {
        if (s[i] == '0') z++;
        else y--;
        max = max > z+y ? max : z+y;
    }
    return max;
}
