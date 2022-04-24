/***************************************************************************************************
 * Copyright: washing
 * FileName: 0868.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-4-24 13:44:39
***************************************************************************************************/

int binaryGap(int n){
    int ret=0;
    int step=0;
    while (n) {
        int end = n % 2;
        n /= 2;
        if (end == 1) {
            ret = fmax(ret, step);
            step = 1;
        } else {
            if (step != 0) step++;
        }
    }
    return ret;
}
