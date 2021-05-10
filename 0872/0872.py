# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/5/10 09:57
# File: 0872.py
# Desc: 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        def parse_tree(root, l):
            if root.left != None:
                parse_tree(root.left, l)
            if root.right != None:
                parse_tree(root.right, l)
            if root.left == None and root.right == None:
                l.append(root.val)

        l1 = []
        l2 = []

        parse_tree(root1, l1)
        parse_tree(root2, l2)

        return l1 == l2