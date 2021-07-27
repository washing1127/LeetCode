# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/27 10:28
# File: 0671.py
# Desc: 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.l = set()
        def parse_tree(root):
            self.l.add(root.val)
            if root.left != None:
                parse_tree(root.left)
                parse_tree(root.right)
        parse_tree(root)
        return sorted(self.l)[1] if len(self.l) > 1 else -1