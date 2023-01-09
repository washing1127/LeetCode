/***************************************************************************************************
 * Copyright: washing
 * FileName: 1806.c
 * Author: washing
 * Version: 1.0
 * Date: 2023-01-09 11:03:03
***************************************************************************************************/


int reinitializePermutation(int n){
    int * l = (int *)malloc(sizeof(int) * n);
    int * l2 = (int *)malloc(sizeof(int) * n);
    for (int i=0;i<n;i++) {
        l[i] = i;
        if (i % 2 == 0) {
            l2[i] = i/2;
        } else {
            l2[i] = n / 2 + (i-1) / 2;
        }
    }
    bool flag = false;
    int ret = 0;
    while (! flag) {
        flag = true;
        for (int i=0;i<n;i++) {
            if (l[i] != l2[i]) flag = false;
            if (l2[i] % 2 == 0) {
                l2[i] = l2[i]/2;
            } else {
                l2[i] = n / 2 + (l2[i]-1) / 2;
            }
        }
        ret++;
    }
    return ret;
}
