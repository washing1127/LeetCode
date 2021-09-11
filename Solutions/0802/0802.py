# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/8/5 11:25
# File: 0802.py
# Desc: 

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        l = set()
        dic = dict()
        for i in range(len(graph)):
            if graph[i] == []: l.add(i)
            else: dic[i] = graph[i]
        l2 = l.copy()
        while True:
            keys = list(dic.keys())
            for i in keys:
                for j in dic[i]:
                    if j not in l:
                        break
                else: 
                    l2.add(i)
                    del dic[i]
            if sorted(list(l2)) == sorted(list(l)):
                break
            else:
                l = l2.copy()

        return sorted(list(l))