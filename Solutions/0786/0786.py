# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/11/29 9:44
# File: 0786.py
# Desc: CV

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left, right = 0.0, 1.0

        while True:
            mid = (left + right) / 2
            i, count = -1, 0
            # 记录最大的分数
            x, y = 0, 1
            
            for j in range(1, n):
                while arr[i + 1] / arr[j] < mid:
                    i += 1
                    if arr[i] * y > arr[j] * x:
                        x, y = arr[i], arr[j]
                count += i + 1

            if count == k:
                return [x, y]
            
            if count < k:
                left = mid
            else:
                right = mid

