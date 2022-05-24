# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/5/24 11:54
# File: 0965.py
# Desc: 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        v = root.val
        self.ret = True
        def parse(root):
            if root.val != v: self.ret = False
            if self.ret and root.left: parse(root.left)
            if self.ret and root.right: parse(root.right)
        parse(root)
        return self.ret
