# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/6/22 17:24
# File: Offer38.py
# Desc: 

class Solution:
    def permutation(self, s: str) -> List[str]:
        se = set()
        s = s + "吊" * (8-len(s))
        for a in range(8):
            for b in range(8):
                if b == a: continue
                for c in range(8):
                    if c in [a,b]: continue
                    for d in range(8):
                        if d in [a,b,c]: continue
                        for e in range(8):
                            if e in [a,b,c,d]: continue
                            for f in range(8):
                                if f in [a,b,c,d,e]: continue
                                for g in range(8):
                                    if g in [a,b,c,d,e,f]: continue
                                    for h in range(8):
                                        if h in [a,b,c,d,e,f,g]: continue
                                        subs = ""
                                        for i in [a,b,c,d,e,f,g,h]:
                                            subs += s[i]
                                        se.add(subs.replace("吊", ""))
        return list(se)
