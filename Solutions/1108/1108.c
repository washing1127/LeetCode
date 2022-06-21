/***************************************************************************************************
 * Copyright: washing
 * FileName: 1108.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-6-21 10:28:21
***************************************************************************************************/

char * defangIPaddr(char * address){
    char * ret = (char *)malloc(sizeof(char) * (strlen(address) + 7));
    int idx = 0;
    for (int i=0; i<strlen(address); i++){
        if (address[i] == '.') {
            ret[idx++] = '[';
            ret[idx++] = '.';
            ret[idx++] = ']';
        } else {
            ret[idx++] = address[i];
        }
    }
    ret[idx] = '\0';
    return ret;
}
