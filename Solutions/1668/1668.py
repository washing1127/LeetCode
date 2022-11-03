# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/03 10:42
# File: 1668.py
# Desc: 


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(word)
        ret = 0
        for i in range(len(sequence)):
            j = i
            temp = 0
            while sequence[j:j+n] == word:
                temp += 1
                j += n
            ret = max(ret, temp)
        return ret
