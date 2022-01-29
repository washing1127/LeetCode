# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/28 10:21
# File: 1996.py
# Desc: CV

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: (x[0], -x[1]))
        ans = 0
        st = []
        for _, def_ in properties:
            while st and st[-1] < def_:
                st.pop()
                ans += 1
            st.append(def_)
        return ans
