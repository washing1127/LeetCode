# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/12/8 16:57
# File: 0020
# Desc: 

class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        s2 = ""

        for i in s:
            if i not in dic:
                s2 += i
            else:
                if not s2.endswith(dic[i]):
                    return False
                else:
                    s2 = s2[:-1]

        return False if s2 else True
