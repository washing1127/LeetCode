/***************************************************************************************************
 * Copyright: washing
 * FileName: 0754.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-11-04 11:32:22
***************************************************************************************************/


int reachNumber(int target){
    target = target > 0 ? target : -target;
    int total = 0;
    int i = 0;
    while (total < target || (total - target) % 2 != 0) {
        i++;
        total += i;
    }
    return i;
}
