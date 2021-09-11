# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/1 10:36
# File: 0022.py
# Desc: 

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        ret = set()
        for s in self.generateParenthesis(n-1):
            for i in range(len(s)):
                ret.add(s[:i]+'()'+s[i:])
        return list(ret)