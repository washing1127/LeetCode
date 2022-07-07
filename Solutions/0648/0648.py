# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/7 10:49
# File: 0648.py
# Desc: 


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=lambda i: len(i))
        dic = dict()
        l = sentence.split(' ')
        for i in l: dic[i] = i
        def parse(l, s):
            for ro in l:
                if s.startswith(ro): return ro
        for k,v in dic.items():
            ret = parse(dictionary, v)
            if ret: dic[k] = ret
        for i in range(len(l)):
            l[i] = dic[l[i]]

        return ' '.join(l)
