# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/5/11 10:39
# File: 0449.py
# Desc: CV


class Codec:
    def serialize(self, root: TreeNode) -> str:
        arr = []
        def postOrder(root: TreeNode) -> None:
            if root is None:
                return
            postOrder(root.left)
            postOrder(root.right)
            arr.append(root.val)
        postOrder(root)
        return ' '.join(map(str, arr))

    def deserialize(self, data: str) -> TreeNode:
        arr = list(map(int, data.split()))
        def construct(lower: int, upper: int) -> TreeNode:
            if arr == [] or arr[-1] < lower or arr[-1] > upper:
                return None
            val = arr.pop()
            root = TreeNode(val)
            root.right = construct(val, upper)
            root.left = construct(lower, val)
            return root
        return construct(-inf, inf)

