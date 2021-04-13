# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/13 11:04
# File: 0783.py
# Desc: 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.m = 100000
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left != None: 
            self.m = min(root.val - self.maxL(root.left), self.m)
            self.minDiffInBST(root.left)
        if root.right != None:
            self.m = min(self.minR(root.right) - root.val, self.m)
            self.minDiffInBST(root.right)
        return self.m


    def maxL(self, root):
        cur = root
        while cur.right != None: cur = cur.right
        return cur.val
    def minR(self, root):
        cur = root
        while cur.left != None: cur = cur.left
        return cur.val