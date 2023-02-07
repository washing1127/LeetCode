# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/2/6 20:21
# File: 2331.py
# Desc: 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def parse(root):
            if root.left:
                l = parse(root.left)
                r = parse(root.right)
                if root.val == 2:
                    return l or r
                else: return l and r
            else:
                return root.val == 1
        return parse(root)
