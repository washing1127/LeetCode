# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/2/7 11:30
# File: 1405.py
# Desc: 

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = ""
        dic = {"a": a, "b": b, "c": c}
        def parse(dic, last):
            values = list(dic.values())
            s = ""
            if values.count(0) == 3: return s, False, dic
            elif values.count(0) == 2:
                for i in "abc":
                    if dic[i] == 0 or i == last: continue
                    elif dic[i] == 1: return i, False, dic
                    elif dic[i] >= 2: return i*2, False, dic
                return s, False, dic
            else:
                li = sorted(dic.items(), key=lambda kv:(kv[1],kv[0]), reverse=True)
                if li[0][0] == last:
                    dic[li[1][0]] -= 1
                    return li[1][0], True, dic
                elif li[0][1] == 1:
                    dic[li[0][0]] -= 1
                    return li[0][0], True, dic
                else:
                    dic[li[0][0]] -= 2
                    return li[0][0]*2, True, dic
        subs = "d"
        while True:
            subs, more, dic = parse(dic, subs[0])
            s += subs
            if not more: break
        return s
