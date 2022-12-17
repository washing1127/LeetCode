# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/17 10:03
# File: 1764.py
# Desc: 

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        l = []
        for i in nums:
            if i >= 0: l.append(str(i))
            else: l.append('+'+str(i)[1:])
        s = '-'.join(l)
        li = []
        for l in groups:
            for idx,i in enumerate(l):
                if i >= 0: l[idx] = str(i)
                else: l[idx] = '+'+str(i)[1:]
            li.append('-'.join(l))
        # li.sort(key = lambda x: x.count('-'), reverse=True)
        while s and li:
            # print(s, li )
            if s.startswith(li[0]):
                s = s[len(li[0])+1:]
                li.pop(0)
            else:
                idx = s.find('-')
                if idx == -1: return False
                else: s = s[idx+1:]
        if not li: return True
        return False
