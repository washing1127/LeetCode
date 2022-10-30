/***************************************************************************************************
 * Copyright: washing
 * FileName: 0481.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-10-31 07:56:07
***************************************************************************************************/

int magicalString(int n){
    if (n <= 3) return 1;
    int *l = (int *)malloc(sizeof(int) * n);
    l[0] = 1;
    l[1] = 2;
    l[2] = 2;
    int ret = 1;
    int gai = 1;
    int idx1 = 2;
    int idx2 = 3;
    for (int i=2; i<n; i++) {
        for (int j=0; j<l[idx1]; j++) {
            l[idx2++] = gai;
            if (gai == 1) ret++;
            if (idx2 == n) return ret;
        }
        idx1++;
        gai = gai % 2 + 1;
    }
    return 0;
}
