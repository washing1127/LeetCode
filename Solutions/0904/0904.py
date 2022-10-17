# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/17 15:18
# File: 0904.py
# Desc: 


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = dict()
        ret = 0
        # print(len(fruits))
        for idx, i in enumerate(fruits):
            if i in d:
                d[i].append(idx)
            elif len(d) < 2: d[i] = [idx]
            else:
                a,b = d.keys()
                ret = max(ret, len(d[a])+len(d[b]))
                d[i] = [idx]
                if d[a][-1] > d[b][-1]:
                    for j in range(len(d[a])):
                        if d[a][j] > d[b][-1]: break
                    # print(j,d[b][-1], d[a])
                    d[a] = d[a][j:]
                    if not d[a]: del d[a]
                    del d[b]
                else:
                    for j in range(len(d[b])):
                        if d[b][j] > d[a][-1]: break
                    # print(j,d[a][-1],d[b])
                    d[b] = d[b][j:]
                    if not d[b]: del d[b]
                    del d[a]
            # print(d)
        if len(d) < 2: return len(list(d.values())[0])
        l1, l2 = d.values()
        ret = max(ret, len(l1)+len(l2))
        return ret
