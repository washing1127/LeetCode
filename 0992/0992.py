# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/9 14:44
# File: 0992.py
# Desc: 

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        if len(set(A)) < K:
            return 0
        count = 0
        end = len(A) - K + 1
        for i in range(end):
            dic = set(A[i:i+K])
            l = len(dic)
            for j in range(i+K-1, len(A)):

                if A[j] not in dic:
                    l += 1
                    dic.add(A[j])
                if l == K:
                    count += 1
                elif l > K:
                    break

        return count