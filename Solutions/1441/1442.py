# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/15 12:58
# File: 1441.py
# Desc: 


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s = set(target)
        num = target[-1]
        ret = []
        for i in range(1, n+1):
            ret.append("Push")
            if i == num: return ret
            if not i in s:
                ret.append("Pop")
