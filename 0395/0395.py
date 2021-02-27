# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/27 7:29
# File: 0395.py
# Desc: 


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        self.longest = 0
        def f(l):
            if not l: return 0
            li = []
            for string in l:
                c = collections.Counter(string)
                for key, v in c.items(): 
                    if v < k:
                        string = string.replace(key, " ")
                if " " in string:
                    for substring in string.split(" "):
                        if len(substring) >= k:
                            li.append(substring)
                else:
                    if len(string) > self.longest: self.longest = len(string)
            return f(li)
        f([s])
        return self.longest 