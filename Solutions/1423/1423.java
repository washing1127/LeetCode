/**
 * @Author: washing
 * @DateTime: 2021/2/6 8:45
 * @File: 1423.java
 * @Desc: 
 **/
class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int total = 0;
        for(int i=0; i<k; i++){
            total += cardPoints[i];
        }
        int max_num = total;
        int length = cardPoints.length;
        for(int i=0; i<k; i++){
            total = total - cardPoints[k-i-1] + cardPoints[length-i-1];
            if (total > max_num) max_num = total;
        }
        return max_num;
    }
}