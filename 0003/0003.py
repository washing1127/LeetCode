# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/12/14 13:41
# File: 0003.py
# Desc: 


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        ans = 0
        l = s[0]
        for i in s:
            if i not in l:
                l += i
            else:
                ans = len(l) if ans < len(l) else ans
                l = l[l.find(i)+1:] + i
        ans = len(l) if ans < len(l) else ans
        return ans