# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/5/8 14:14
# File: 1723.py
# Desc: 
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def check(jobs, k, limit):
            works = [0] * k
            return back(jobs, works, 0, limit)

        def back(jobs, works, i, limit):
            if i >= len(jobs): return True
            cur = jobs[i]
            for j in range(len(works)):
                if works[j] + cur <= limit:
                    works[j] += cur
                    if back(jobs, works, i+1, limit): 
                        return True
                    works[j] -= cur
                if works[j] == 0 or works[j] + cur == limit:
                    break
            return False

        jobs.sort(reverse=True)
        l = jobs[0]
        r = sum(jobs)
        while l < r:
            mid = (l + r) >> 1
            if check(jobs, k, mid):
                r = mid
            else: 
                l = mid + 1
        return l
