# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/17 10:06
# File: 1302.py
# Desc: 



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.lev = 0
        self.ret = 0
        def parse(root, lev=0):
            if lev > self.lev:
                self.ret = root.val
                self.lev = lev
            elif lev == self.lev:
                self.ret += root.val
            if root.left: parse(root.left, lev+1)
            if root.right: parse(root.right, lev+1)
        parse(root)
        return self.ret
