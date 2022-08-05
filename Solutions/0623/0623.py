# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/08/05 11:54
# File: 0623.py
# Desc: 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1: return TreeNode(val, left=root)
        def parse(root,nextlevel=2):
            if nextlevel == depth:
                l = root.left
                r = root.right
                root.left = TreeNode(val, left=l)
                root.right = TreeNode(val, right=r)
            elif nextlevel < depth:
                if root.left: parse(root.left, nextlevel+1)
                if root.right: parse(root.right, nextlevel+1)
        parse(root)
        return root

