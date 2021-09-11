# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/5 17:16
# File: 0841.py
# Desc: 

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        s = set()
        l = [rooms[0]]
        N = len(rooms)
        while l != []:
            now = l.pop()
            for key in now:
                if not key in s:
                    s.add(key)
                    l.append(rooms[key])
        for i in range(1, N):
            if not i in s: return False
        return True
