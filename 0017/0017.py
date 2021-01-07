# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/01/07 17:15
# File: 0017.py
# Desc: 


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        dic = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        li = [i for i in dic[digits[0]]]
        for i in digits[1:]:
            li_length = len(li)
            mapping = dic[i]
            li *= len(mapping)
            for idx in range(len(li)):
                c = idx//li_length
                print(idx, c, mapping)
                s = mapping[c]
                li[idx] = li[idx] + s
        return li