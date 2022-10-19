# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/19 10:35
# File: 1700.py
# Desc: 


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s = collections.Counter(students)
        while sandwiches and sandwiches[0] in s:
            s[sandwiches[0]] -= 1
            if s[sandwiches[0]] == 0:
                del s[sandwiches[0]]
            sandwiches.pop(0)
        # print(s)
        if s:
            return list(s.values())[0]
        return 0
