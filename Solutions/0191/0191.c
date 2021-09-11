// Author: washing
// DateTime: 2021/3/22 10:24
// File: 0191.c
// Desc: 

int hammingWeight(uint32_t n) {
    int a=0;
    while (n > 0){
        a += n%2;
        n /= 2;
    }
    return a;
}