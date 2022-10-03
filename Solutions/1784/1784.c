/***************************************************************************************************
 * Copyright: washing
 * FileName: 1784.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-10-3 11:13:36
***************************************************************************************************/

bool checkOnesSegment(char * s){
    bool flag = true;
    for (int i=0; i<strlen(s); i++){
        if (s[i]=='1') {
            if (!flag) return false;
        } else flag = false;
    }
    return true;
}
