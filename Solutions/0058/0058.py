# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/11 12:06
# File: 0058.py
# Desc: 
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        
        if not s: return 0
        return len(s.split(' ')[-1])
        
        # return len(s) - 1 - s.rfind(' ')
        
        # if not s: return 0
        # l = 0
        # for i in range(len(s)-1, -1, -1):
        #     c = s[i]
        #     if c == ' ': break
        #     l += 1
        # return l