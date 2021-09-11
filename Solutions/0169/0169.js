// Author: washing
// DateTime: 2021/1/26 18:42
// File: 0169.js
// Desc: 


/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    var a = 0;
    var c = 0;
    var n;
    for (var i=0; i<nums.length; i++){
        n = nums[i];
        if (c==0){
            a = n;
            c++;
        }else if (a==n){
            c++;
        }else{
            c--;
        }
    }
    return a;
};