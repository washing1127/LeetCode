# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/3/8 20:21
# File: 2185.py
# Desc: 


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum([1 for i in words if i.startswith(pref)])
