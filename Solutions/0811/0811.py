# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/5 07:18
# File: 0811.py
# Desc: 


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        c = dict()
        for i in cpdomains:
            num, s = i.split(' ')
            l = s.split('.')
            num = int(num)
            for i in range(len(l)):
                s2 = '.'.join(l[i:])
                if s2 in c:
                    c[s2] += num
                else: c[s2] = num
        return [str(v)+' '+k for k,v in c.items()]
