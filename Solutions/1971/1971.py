# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/19 10:41
# File: 1971.py
# Desc: 

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination: return True
        s = set()
        s.add(source)
        while True:
            del_list = []
            for idx,(a,b) in enumerate(edges):
                if a in s or b in s:
                    s.add(a)
                    s.add(b)
                    del_list.append(idx)
            # print(del_list)
            for idx in del_list[::-1]: edges.pop(idx)
            if destination in s: return True
            if not edges or not del_list: return False
