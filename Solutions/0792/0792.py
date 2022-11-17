# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/17 8:48
# File: 0792.py
# Desc: 


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = dict()
        for idx, i in enumerate(s):
            if not i in d: d[i] = [1]
            d[i].append(idx)
        ret = 0
        for word in words:
            temp_idx = 0
            for k in d.keys(): d[k][0] = 1
            for c in word:
                if not c in d: break
                flag = False
                l = d[c][0]
                r = len(d[c]) -1
                while l < r:
                    m = (l+r) // 2
                    if d[c][m] < temp_idx: l = m+1
                    else: r = m
                d[c][0] = l+1
                # print(d[c],l)
                # if : break
                if l < len(d[c]) and d[c][l] >= temp_idx:
                    temp_idx = d[c][l]
                    flag = True
                else: break
            else: ret+=1

        return ret
