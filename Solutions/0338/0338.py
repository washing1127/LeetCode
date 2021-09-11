# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/3/3 8:35
# File: 0338.py
# Desc: 


class Solution:
    def countBits(self, num: int) -> List[int]:
        li = []
        for i in range(num+1):
            li.append(bin(i).count("1"))
        return li