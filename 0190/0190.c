// Author: washing
// DateTime: 2021/3/29 16:54
// File: 0190.c
// Desc: 

uint32_t reverseBits(uint32_t n) {
    long ans = 0;
    int res;
    for (int i=0; i<32; i++){
        res = n % 2;
        ans <<= 1;
        ans += res;
        n >>= 1;
    }
    return ans;
}