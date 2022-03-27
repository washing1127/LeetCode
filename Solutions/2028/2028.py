# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/3/27 15:16
# File: 2028.py
# Desc: 

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (len(rolls)+n)
        sumn = total - sum(rolls)
        if sumn < n or sumn > n*6: return []
        ret = [int(sumn/n)] * n
        rest = sumn - sum(ret)
        for i in range(rest):
            ret[i] += 1
        return ret

