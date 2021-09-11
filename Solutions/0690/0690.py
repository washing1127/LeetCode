# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/5/1 21:16
# File: 0690.py
# Desc: 

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        for i in employees:
            if i.id == id:
                leader = i
                break

        emp_set = set(leader.subordinates)
        a = len(emp_set) - 1
        while a != len(emp_set):
            a = len(emp_set)
            for emp in employees:
                if emp.id in emp_set and emp.subordinates != []:
                    for sub in emp.subordinates:
                        emp_set.add(sub)
                        
        ret = leader.importance
        for i in employees:
            if i.id in emp_set:
                ret += i.importance
        
        return ret