/***************************************************************************************************
 * Copyright: washing
 * FileName: 0779.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-10-20 14:56:57
***************************************************************************************************/


int kthGrammar(int n, int k){
    long int changdu = pow(2, n-1);
    if (k == 0) k = changdu;
    if (n <= 3) {
        int l[4] = {0,1,1,0};
        return l[k-1];
    }
    int yiban = changdu / 2;
    if (k-1 < yiban) return kthGrammar(n-1, k);
    else return kthGrammar(n-1, ((k%yiban)+yiban/2)%yiban);
}
