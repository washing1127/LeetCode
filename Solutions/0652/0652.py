# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/9/5 10:37
# File: 0652.py
# Desc: 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.ret = list()
        self.set = set()
        self.set2 = set()
        def parse(root):
            if not root: return (None,)
            a = parse(root.left)
            b = parse(root.right)
            if a != (None,) or b != (None,):
                l = (root.val,) + a + b
            else:
                l = (root.val,)
            # print(l)
            if l in self.set:
                if not l in self.set2:
                    self.ret.append(root)
                    self.set2.add(l)
            else: self.set.add(l)
            return l
        parse(root)
        return list(set(self.ret))
