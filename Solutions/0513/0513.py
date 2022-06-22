# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/6/22 10:51
# File: 0513.py
# Desc: 



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.ret = [root.val, 0, 0]
        def parse(root, zy=0, deep=0):
            if deep > self.ret[2]:
                self.ret = [root.val, zy, deep]
            elif deep == self.ret[2] and zy < self.ret[1]:
                self.ret = [root.val, zy, deep]
            if root.left:
                parse(root.left, zy-1, deep+1)
            if root.right:
                parse(root.right, zy+1, deep+1)
        parse(root)
        return self.ret[0]
