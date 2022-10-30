# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/30 10:24
# File: 0784.py
# Desc: 


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ret = []
        for i in s:
            new_l = list()
            if i.isalpha():
                if not ret:
                    new_l.append(i.lower())
                    new_l.append(i.upper())
                else:
                    for j in ret:
                        new_l.append(j+i.lower())
                        new_l.append(j+i.upper())
            else:
                if not ret:
                    new_l.append(i)
                else:
                    for j in ret:
                        new_l.append(j+i)
            ret = new_l
        return ret
