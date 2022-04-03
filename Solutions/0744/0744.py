# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/4/3 10:49
# File: 0744.py
# Desc: 

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if i > target: return i
        return letters[0]
