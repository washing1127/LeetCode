# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/3/21 09:49
# File: 0653.py
# Desc: 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.s = set()
        self.flag = False
        def parse(root):
            if k - root.val in self.s:
                self.flag = True
            self.s.add(root.val)
            if root.left: parse(root.left)
            if root.right: parse(root.right)
        if root: parse(root)
        return self.flag
