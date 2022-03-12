# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/3/12 10:40
# File: 0590.py
# Desc: 

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.li = []
        def parse(root):
            if root.children:
                for child in root.children: parse(child)
            self.li.append(root.val)
        if not root: return []
        parse(root)
        return self.li
