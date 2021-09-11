# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/5/26 15:30
# File: 1190.py
# Desc: 

class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        idx1 = s.find("(")
        if idx1 == -1: return s
        counter = 1
        for i in range(idx1+1, len(s)):
            c = s[i]
            if c == "(": counter += 1
            elif c == ")": counter -= 1
            else: continue

            if counter == 0:
                idx2 = i 
                break
        a = s[:idx1]
        b = s[idx2-1:idx1:-1].replace("(", "-").replace(")","(").replace("-", ")")
        c = s[idx2+1:]

        return a + self.reverseParentheses(b) + self.reverseParentheses(c)
