/**
 * @Author: washing
 * @DateTime: 2021/01/22 12:44
 * @File: 0989.java
 * @Desc: 
 **/
class Solution {
    public List<Integer> addToArrayForm(int[] A, int K) {
            List lk = new ArrayList();
            List ret = new ArrayList();
            int plus = 0;
            if (K==0){
                lk.add(0,0);
            }
            while (K != 0) {
                lk.add(0, K%10);
                K = K / 10;
            }
            int a = A.length-1;
            int k = lk.size()-1;
            if (a < 0) {
                return lk;
            } else {
                while (a>=0 && k>=0){
                    int num = A[a] + (int)lk.get(k) + plus;
                    plus = num / 10;
                    ret.add(0, num%10);
                    a--; k--;
                }
                while (a>=0) {
                    int num = A[a] + plus;
                    plus = num / 10;
                    ret.add(0, num%10);
                    a--;
                }
                while (k>=0) {
                    int num = (int)lk.get(k) + plus;
                    plus = num / 10;
                    ret.add(0, num%10);
                    k--;
                }
                if (plus!=0) {
                    ret.add(0, plus);
                } 
            }
            return ret;
    }
}