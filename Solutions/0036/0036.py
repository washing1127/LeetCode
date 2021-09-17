# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/9/17 14:40
# File: 0036.py
# Desc: 

import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        npb = np.asarray(board)
        for i in range(9):
            cs = []
            cs.append(collections.Counter(npb[i]))
            cs.append(collections.Counter(npb[:,i]))
            if i in [0, 3, 6]:
                for j in [0, 3, 6]:
                    cs.append(collections.Counter(npb[i:i+3, j:j+3].reshape(9)))
            for c in cs:
                for k, v in c.items():
                    if v>1 and k!=".": return False
        return True
