# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/6/23 10:10
# File: 0030
# Desc: 

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        c = collections.Counter(words)
        n = len(words[0])
        ret = []
        for i in range(len(s)-n*len(words)+1):
            c2 = copy.copy(c)
            idx = i
            while c2[s[idx:idx+n]]:
                c2[s[idx:idx+n]] -= 1
                if not c2[s[idx:idx+n]]:
                    del c2[s[idx:idx+n]]
                idx += n
            if not c2: ret.append(i)
        return ret
