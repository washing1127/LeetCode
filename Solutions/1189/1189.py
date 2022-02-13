# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/2/13 15:30
# File: 1189.py
# Desc: 

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = collections.Counter(text)
        ret = 10000
        d = {'b':1,'a':1,'l':2,'o':2,'n':1}
        for i in 'balon':
            ret = min(ret, c[i]//d[i])
        return ret
