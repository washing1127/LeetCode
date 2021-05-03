# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/05/03 13:22
# File: 0007.py
# Desc: 

class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s.startswith("-"):
            s = '-' + s[1:][::-1]
        else:
            s = s[::-1]
            
        ans = int(s)
        
        if -2147483648 > ans or 2147483647 < ans:
            ans = 0
        
        return ans
