# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/5/1 10:06
# File: 1305.py
# Desc: 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.l1 = []
        self.l2 = []
        def parse(node, tp=1):
            if node.left: parse(node.left, tp=tp)
            if tp == 1: self.l1.append(node.val)
            else: self.l2.append(node.val)
            if node.right: parse(node.right, tp=tp)
        if root1: parse(root1)
        if root2: parse(root2, 2)
        ret = []
        while self.l1 and self.l2:
            if self.l1[0] < self.l2[0]:
                ret.append(self.l1.pop(0))
            else: ret.append(self.l2.pop(0))
        ret.extend(self.l1)
        ret.extend(self.l2)
        return ret
