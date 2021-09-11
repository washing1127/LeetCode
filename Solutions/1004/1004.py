# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/19 17:11
# File: 1004.py
# Desc: 

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:

        # # others
        count = 0
        left = 0

        for i in A:
            if i == 0: count += 1
            if count > K:
                if A[left] == 0: count -= 1
                left += 1
        return len(A) - left

        # # mine
        # if K >= A.count(0): return len(A)
        # l = []
        # count = 0
        # flag = A[0]
        # labal = -1 if flag == 0 else 1
        # for i in A:
        #     if i != flag:
        #         l.append(count*labal)
        #         labal *= -1
        #         count = 1
        #         flag = i
        #     else:
        #         count += 1
        # l.append(count*labal)
        # max_total = 0
        # for idx in range(len(l)):
        #     num = l[idx]
        #     k = K
        #     if num >= 0:
        #         total = num
        #         for idx2 in range(idx+1, len(l), 2):
        #             total += min(-l[idx2], k) 
        #             k += l[idx2]
        #             if k < 0: break
        #             if idx2 < len(l) - 1:
        #                 total += l[idx2+1]
        #         else:
        #             if k>=0 and idx>=1:
        #                 total += min(-l[idx-1], k)
        #         if total > max_total: max_total = total
        # return max_total