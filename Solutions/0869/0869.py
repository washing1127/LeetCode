# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/10/28 10:49
# File: 0869.py
# Desc: 

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # se = set()
        # for i in range(30):
        #     se.add(''.join(sorted(str(2**i))))
        # return ''.join(sorted(str(n))) in se
        return ''.join(sorted(str(n))) in [''.join(sorted(str(2**i))) for i in range(30)]
