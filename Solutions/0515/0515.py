# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/6/24 10:51
# File: 0515.py
# Desc: 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.l = []
        def parse(root, level=0):
            if len(self.l) <= level:
                self.l.append(root.val)
            else:
                self.l[level] = max(self.l[level], root.val)
            if root.left: parse(root.left, level+1)
            if root.right: parse(root.right, level+1)
        if root: parse(root)
        return self.l
