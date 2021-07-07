# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/7 11:08
# File: 1711.py
# Desc: 


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        ms = max(deliciousness) * 2
        ret = 0
        mp = dict()
        for val in deliciousness:
            s = 1
            while s <= ms:
                count = mp.get(s - val, 0)
                ret += count
                s <<= 1
            mp[val] = mp.get(val, 0) + 1
        return ret % 1000000007
