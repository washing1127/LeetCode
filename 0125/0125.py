# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/17 15:11
# File: 0125.py
# Desc: 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([i for i in s if (i.isalpha() or i.isdigit())]).lower()
        if s == s[::-1]: return True
        else: return False