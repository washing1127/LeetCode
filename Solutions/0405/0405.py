# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/10/2 12:08
# File: 0405.py
# Desc: 

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return '0'
        if num > 0: negative = False
        else: negative = True
        num = abs(num)
        kvdic = {
            0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f',
        }
        vkdic = {}
        for k, v in kvdic.items(): vkdic[v] = k

        s = ''
        while num > 0:
            s = kvdic[num % 16] + s
            num //= 16
        if not negative: return s
        s = '0'*(8-len(s))+s
        ret = ''
        plus = 1
        for i in s[::-1]:
            k = 15-vkdic[i]+plus
            plus = k // 16
            if k>=16:
                k = k % 16
            ret = kvdic[k] + ret
        return ret
