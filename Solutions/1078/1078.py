# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/12/26 11:05
# File: 1078.py
# Desc: 

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        w = text.split(" ")
        ret = []
        for i in range(2,len(w)):
            if w[i-2] == first and w[i-1] == second: ret.append(w[i])
        return ret
