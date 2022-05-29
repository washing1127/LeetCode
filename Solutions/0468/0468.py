# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/5/29 8:56
# File: 0468.py
# Desc: 

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            l = queryIP.split(".")
            if len(l) == 4:
                flag = True
                for i in l:
                    if not i.isdigit():
                        flag = False
                        break
                    j = int(i)
                    if 0 > j  or j > 255 or str(j) != i:
                        flag = False
                        break
                if flag: return 'IPv4'
        elif ':' in queryIP:
            l = queryIP.split(":")
            if len(l) == 8:
                # print(l)
                flag = True
                for i in l:
                    if not re.fullmatch('[0-9a-fA-F]{1,4}', i):
                        # print(i)
                        flag = False
                        break
                if flag: return 'IPv6'
        return 'Neither'
