# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/20 16:24
# File: 0779.py
# Desc: 

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        changdu = 2 ** (n-1)
        if k == 0: k=changdu
        if n <= 3:
            return int('0110'[k-1])
        # print(n, changdu, k)
        yiban = changdu // 2
        if k-1 < yiban :
            return self.kthGrammar(n-1, k)
        else:
            return self.kthGrammar(n-1, ((k%yiban)+yiban//2)%yiban)
