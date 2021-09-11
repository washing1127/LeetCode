// Author: washing
// DateTime: 2021/1/26 18:43
// File: 0169.kt
// Desc: 

class Solution {
    fun majorityElement(nums: IntArray): Int {
        var c = 0
        var a = 0
        for (n in nums){
            if (c == 0){
                a = n
                c += 1
            }else if(a == n){
                c += 1
            }else {
                c -= 1
            }
        }
        return a
    }
}