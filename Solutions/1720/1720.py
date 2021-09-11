# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/5/6 20:25
# File: 1720.py
# Desc: 
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        def th(a, b):
            sa = bin(a)[2:]
            sb = bin(b)[2:]
            la = len(sa)
            lb = len(sb)
            if la < lb:
                sa = "0" * (lb-la) + sa
            elif lb < la:
                sb = "0" * (la-lb) + sb
            ret = "0b"
            for i, j in zip(sa, sb):
                if j == "0":
                    ret += i
                else:
                    ret += "1" if i == "0" else "0"
            return int(ret, 2)

        li = [first]
        for num in encoded:
            end = li[-1]
            decoded = th(end, num)
            li.append(decoded)

        return li