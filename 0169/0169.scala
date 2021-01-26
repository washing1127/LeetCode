// Author: washing
// DateTime: 2021/1/26 18:48
// File: 0169.scala
// Desc: 

object Solution {
    def majorityElement(nums: Array[Int]): Int = {
        var a=0;
        var c=0;
        
        for (n <- nums) {
            if (c==0){
                a = n
                c += 1
            } else if (a==n){
                c += 1
            } else {
                c -= 1
            }
        }
        return a
    }
}