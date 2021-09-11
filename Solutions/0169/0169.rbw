# Author: washing
# DateTime: 2021/1/26 18:45
# File: 0169.rbw
# Desc: 

# @param {Integer[]} nums
# @return {Integer}
def majority_element(nums)
    c=0
    for i in nums
        if c==0
            a=i
            c=c+1
        elsif a==i
            c=c+1
        else
            c=c-1
        end
    end
    return a
end