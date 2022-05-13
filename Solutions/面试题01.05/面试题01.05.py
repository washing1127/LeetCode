# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/5/13 10:50
# File: 面试题 01.05.py
# Desc: 


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        i = 0
        j = 0
        if len(first+second) == 1: return True
        if abs(len(first) - len(second)) >= 2: return False
        can_pass = True
        while i < len(first) and j < len(second):
            if first[i] != second[j]:
                if can_pass:
                    if len(first) < len(second):
                        j += 1
                    elif len(first) > len(second):
                        i += 1
                    else:
                        i += 1
                        j += 1
                    can_pass = False
                else:
                    return False
            else:
                i += 1
                j += 1
        if i < len(first)-1 or j < len(second)-1: return False
        return True
