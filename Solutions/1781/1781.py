# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/12 11:17
# File: 1781.py
# Desc: 


class Solution:
    def beautySum(self, s: str) -> int:
        if len(s) <= 2: return 0
        ret = 0
        old_li = dict()
        for c in 'abcdefghijklmnopqrstuvwxyz':
            old_li[c] = 0
        old_li[s[0]] += 1
        old_li[s[1]] += 1
        for r in range(2,len(s)):
            old_li[s[r]] += 1
            li = None
            for j in range(len(s)-r):
                if li is None:
                    li = old_li.copy()
                else:
                    print(",,,,,",end=' ')
                    li[s[j-1]] -= 1
                    li[s[j+r]] += 1
                v = [i for i in li.values() if i != 0]
                ret += max(v) - min(v)
            #     print(max(v), min(v))
            #     print(j,r,s,s[j:j+r],s[j-1],s[j+r],li)
            # print('=================')
        return ret
