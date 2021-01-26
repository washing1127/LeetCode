// Author: washing
// DateTime: 2021/1/26 18:48
// File: 0169.ts
// Desc: 


function majorityElement(nums: number[]): number {
    var a=0;
    var c=0;
    var n: number;
    for (var i=0;i<nums.length;i++){
        n = nums[i];
        if (c==0){
            a=n;
            c+=1;
        }else if(a==n){
            c+=1;
        }else{
            c-=1;
        }
    }
    return a;
}