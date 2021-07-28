# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/28 15:28
# File: 0863.py
# Desc: 

class Solution:
    def distanceK(self, root:TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = list()
        self.parents = dict()
        self.parents[root.val] = None
        def findParents(node):
            if node.left != None:
                self.parents[node.left.val] = node
                findParents(node.left)
            if node.right != None:
                self.parents[node.right.val] = node
                findParents(node.right)
        def findAns(node, fr, depth, k):
            if node == None: return
            if depth == k: 
                ans.append(node.val)
                return
            if node.left != fr:
                findAns(node.left, node, depth+1, k)
            if node.right != fr:
                findAns(node.right, node, depth+1, k)
            if self.parents[node.val] != fr:
                findAns(self.parents[node.val], node, depth+1, k)
        findParents(root)
        findAns(target, None, 0, k)

        return ans
