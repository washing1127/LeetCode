# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/8/23 15:42
# File: 0443.py
# Desc: 

class Solution:
    def compress(self, chars: List[str]) -> int:
        step = 0
        idx = 0
        while step < len(chars):
            temp = 1
            while step+temp<len(chars) and chars[step] == chars[step+temp]:
                temp += 1
            # print(idx, step, temp)
            if temp > 1:
                s = chars[step] + str(temp)
                for i in s:
                    chars[idx] = i 
                    idx += 1
            else:
                chars[idx] = chars[step]
                idx += 1
            step += temp
        # print(chars)
        return idx