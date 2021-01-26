// Author: washing
// DateTime: 2021/1/26 18:51
// File: 0169.go
// Desc: 

func majorityElement(nums []int) int {
    var a, c, n int = 0, 0, 0
    for i := 0; i<len(nums); i++ {
        n = nums[i]
        if c == 0 {
            a = n
            c++
        }else if a == n {
            c++
        }else {
            c--
        }
    }
    return a
}