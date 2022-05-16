# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/5/16 10:50
# File: 面试题 04.06.py
# Desc: 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        self.l = []
        def parse(root):
            if root.left: parse(root.left)
            self.l.append(root)
            if root.right: parse(root.right)
        if root: parse(root)
        if p in self.l:
            index = self.l.index(p)+1
            if index < len(self.l):
                return self.l[index]
        return None
