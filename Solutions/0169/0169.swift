// Author: washing
// DateTime: 2021/1/26 18:48
// File: 0169.swift
// Desc: 


class Solution {
    func majorityElement(_ nums: [Int]) -> Int {
        var a = 0
        var c = 0
        for n in nums {
            if c == 0 {
                a = n
                c+=1
            } else if a == n {
                c+=1
            } else {
                c-=1
            }
        }
        return a
    }
}