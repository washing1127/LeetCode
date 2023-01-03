# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/1/03 10:02
# File: 2042.py
# Desc: 


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        p = re.compile("\d*")
        li = p.findall(s)
        li = [int(i) for i in li if i != ""]
        for i in range(1,len(li)):
            if li[i] <= li[i-1]: return False
        return True
