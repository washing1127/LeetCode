# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/3/12 14:09
# File: 0331.py
# Desc: 

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        li = preorder.split(",")
        length = len(li)
        if preorder == "#": return True
        elif preorder.startswith("#"): return False
        if length < 3 or length % 2 == 0: return False

        trans = li[:2].copy()
        for i in li[2:]:
            trans.append(i)
            while trans[-2:] == ["#", "#"]:
                if len(trans) == 2: return False
                trans = trans[:-3] + ["#"]

        if trans == ["#"]: return True
        else: return False