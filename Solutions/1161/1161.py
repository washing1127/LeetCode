# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/30 10:42
# File: 1161.py
# Desc: 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.l = []
        def parse(root,level=0):
            if level >= len(self.l): self.l.append(0)
            self.l[level] += root.val
            if root.left: parse(root.left, level+1)
            if root.right: parse(root.right, level+1)
        parse(root)
        m = max(self.l)
        for i,num in enumerate(self.l):
            if num == m: return i+1
