// Author: washing
// DateTime: 2023/2/4 18:52
// File: 1798.java
// Desc: 


class Solution {
    public int getMaximumConsecutive(int[] coins) {
        int res = 1;
        Arrays.sort(coins);
        for (int i : coins) {
            if (i > res) {
                break;
            }
            res += i;
        }
        return res;
    }
}

// 作者：力扣官方题解
// 链接：https://leetcode.cn/problems/maximum-number-of-consecutive-values-you-can-make/solutions/2090079/ni-neng-gou-zao-chu-lian-xu-zhi-de-zui-d-wci4/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
