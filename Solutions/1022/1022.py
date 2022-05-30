# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/5/30 16:09
# File: 1022.py
# Desc: 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ret = 0
        def parse(root, lastnum=0):
            lastnum *= 2
            lastnum += root.val
            if root.left: parse(root.left, lastnum)
            if root.right: parse(root.right, lastnum)
            if not root.left and not root.right: self.ret += lastnum
        if root: parse(root)
        return self.ret
