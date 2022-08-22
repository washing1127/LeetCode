# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/22 09:49
# File: 0655.py
# Desc: 


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def calDepth(node: Optional[TreeNode]) -> int:
            return max(calDepth(node.left) + 1 if node.left else 0, calDepth(node.right) + 1 if node.right else 0)
        height = calDepth(root)

        m = height + 1
        n = 2 ** m - 1
        ans = [[''] * n for _ in range(m)]
        def dfs(node: Optional[TreeNode], r: int, c: int) -> None:
            ans[r][c] = str(node.val)
            if node.left:
                dfs(node.left, r + 1, c - 2 ** (height - r - 1))
            if node.right:
                dfs(node.right, r + 1, c + 2 ** (height - r - 1))
        dfs(root, 0, (n - 1) // 2)
        return ans

