# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/6/4 18:11
# File: 0929.py
# Desc: 


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for i in emails:
            a, b = i.split("@")
            a = a.split("+")[0].replace(".", "")
            s.add("@".join([a,b]))
        return len(s)
