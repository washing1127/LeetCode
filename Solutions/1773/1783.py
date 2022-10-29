# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/29 10:17
# File: 1773.py
# Desc: 


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ret = 0
        if ruleKey == 'type': i = 0
        elif ruleKey == 'color': i = 1
        else: i = 2
        for j in items:
            if j[i] == ruleValue: ret += 1
        return ret
