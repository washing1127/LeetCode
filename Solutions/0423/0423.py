# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/11/24 12:04
# File: 0423.py
# Desc: 


class Solution:
    def originalDigits(self, s: str) -> str:
        c = collections.Counter(s)
        dic = dict()
        dic['0'] = c['z']
        dic['2'] = c['w']
        dic['4'] = c['u']
        dic['6'] = c['x']
        dic['8'] = c['g']
        dic['1'] = c['o'] - dic['0'] - dic['2'] - dic['4']
        dic['3'] = c['t'] - dic['2'] - dic['8']
        dic['5'] = c['f'] - dic['4']
        dic['7'] = c['v'] - dic['5']
        dic['9'] = c['i'] - dic['5'] - dic['6'] - dic['8']
        ret = ''
        for i in range(10):
            ret += dic[str(i)] * str(i)
        return ret
