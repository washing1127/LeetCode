# coding=utf-8
# /usr/bin/env python
"""
Author：washing
date：2021/4/16 14:31
desc: 0087.py
"""
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def dfs(i1, i2, length):
            if s1[i1:i1+length] == s2[i2:i2+length]:
                return True

            if Counter(s1[i1:i1+length]) != Counter(s2[i2:i2+length]):
                return False

            for i in range(1, length):
                if dfs(i1, i2, i) and dfs(i1 + i, i2 + i, length - i):
                if dfs(i1, i2 + length - i, i) and dfs(i1 + i, i2, length - i):
                    return True
        
            return False

        ans = dfs(0, 0, len(s1))
        dfs.cache_clear()
        return ans
