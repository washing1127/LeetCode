# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/8/9 14:09
# File: 0313.py
# Desc: 

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        m = len(primes)
        pointers = [1] * m

        for i in range(2, n + 1):
            min_num = min(dp[pointers[j]] * primes[j] for j in range(m))
            dp[i] = min_num
            for j in range(m):
                if dp[pointers[j]] * primes[j] == min_num:
                    pointers[j] += 1
        
        return dp[n]