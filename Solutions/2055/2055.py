# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/3/8 11:21
# File: 2055.py
# Desc: 

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        l = []
        for idx,c in enumerate(s):
            if c == '|':
                l.append(idx)
        # print(l)
        ret = []
        for a, b in queries:
            if not l:
                ret.append(0)
                continue
            la=lb=0; ra=rb=len(l)-1
            while la < ra:
                m = (la+ra)//2
                if l[m] >= a: ra=m
                else: la=m+1
            while lb < rb:
                m = (lb+rb)//2
                if l[m] >= b: rb=m
                else: lb=m+1
            if l[lb] > b: lb-=1
            # print(la,lb)
            if lb<=la: ret.append(0)
            else:
                ret.append(l[lb]-l[la]-(lb-la))
        return ret

        # l = ""
        # for c in s:
        #     if c == '*': l += "0"
        #     else: l += "1"
        # ret = []
        # for a,b in queries:
        #     subs = l[a:b+1]
        #     sm = subs.count("1")
        #     if sm<2:
        #         ret.append(0)
        #         continue
        #     left = subs.index('1')
        #     right = subs.rindex('1')
        #     ret.append(right+1-left-sm)
        # return ret
