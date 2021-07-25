# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/25 13:57
# File: 1743.py
# Desc: 

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dic = {}
        for a in adjacentPairs:
            if a[0] not in dic.keys():
                dic[a[0]] = [a[1]]
            else:
                dic[a[0]].append(a[1])
            if a[1] not in dic.keys():
                dic[a[1]] = [a[0]]
            else:
                dic[a[1]].append(a[0])
        for k in dic.keys():
            if len(dic[k]) == 1:
                break
        ans = [k]
        last_k = k
        k=dic[k][0]
        while len(dic[k])!=1:
            ans.append(k)
            tmp_k = k
            for i in range(len(dic[k])): 
                if dic[k][i]!=last_k:
                    k = dic[k][i]
                    break
            last_k = tmp_k
        ans.append(k)
        return ans
