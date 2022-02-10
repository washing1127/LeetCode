# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/2/10 10:03
# File: 1447.py
# Desc: 

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ret = []
        done_set = set()
        for fm in range(2,n+1):
            for fz in range(1,fm):
                shang = f"{fz/fm:.9f}"
                if shang in done_set: continue
                else:
                    ret.append(f"{fz}/{fm}")
                    done_set.add(shang)
        return ret
