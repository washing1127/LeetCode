# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/31 13:36
# File: 0987.py
# Desc: 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.dic = dict()
        def parse(root, row, col):
            if col not in self.dic.keys(): 
                self.dic[col] = dict()
            if row not in self.dic[col].keys():
                self.dic[col][row] = []
            self.dic[col][row].append(root.val)
            if root.left != None:
                parse(root.left, row+1, col-1)
            if root.right != None:
                parse(root.right, row+1, col+1)
        parse(root, 0, 0)
        ret = []
        cols = list(self.dic.keys())
        cols.sort()
        for col in cols:
            ret.append([])
            rows = list(self.dic[col])
            rows.sort()
            for row in rows:
                ret[-1] += sorted(self.dic[col][row])

        return ret
