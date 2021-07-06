# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/6 11:13
# File: 1418.py
# Desc: 

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        l = []
        dic = dict()
        for cName, tNum, fItem in orders:
            if not tNum in dic.keys(): dic[tNum] = {fItem: 1}
            elif not fItem in dic[tNum].keys(): dic[tNum][fItem] = 1
            else: dic[tNum][fItem] += 1
            if not fItem in l: l.append(fItem)
        l.sort()
        ret = [["Table"]+l]
        keys = sorted(dic, key=lambda i: int(i))
        for tNum in keys:
            tlist = [tNum]
            for fItem in l:
                tlist.append(str(dic[tNum].get(fItem, 0)))
            ret.append(tlist)
        return ret
