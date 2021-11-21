# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/11/21 11:30
# File: 0559.py
# Desc: 

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        children = [root]
        ret = 0
        while True:
            flag = False
            l = list()
            for i in children:
                if i: 
                    flag = True
                    l += i.children
            if flag:
                ret += 1
            else: break
            children = l
        return ret
