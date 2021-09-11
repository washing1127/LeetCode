# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/5/15 10:33
# File: 0013.py
# Desc: 


class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "1": 4,
            "2": 9,
            "3": 40,
            "4": 90,
            "5": 400,
            "6": 900,
        }

        s = s.replace("IV","1").replace("IX","2").replace("XL","3").replace("XC","4").replace("CD","5").replace("CM","6")

        ret = 0

        for i in s:
            ret += dic[i]

        return ret