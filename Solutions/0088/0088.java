// Author: washing
// DateTime: 2021/4/5 19:12
// File: 0088.java
// Desc: 

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if (n==0) return;
        int[] l = new int [m];
        int[] r = new int [n];
        for (int i=0; i<m; i++){
            l[i] = nums1[i];
        }
        for (int j=0; j<n; j++){
            r[j] = nums2[j];
        }

        int i = 0;
        int j = 0;
        for (int k=0; k<nums1.length; k++){
            if (j >= n || i < m && l[i] <= r[j]){
                nums1[k] = l[i];
                i++;
            }else {
                nums1[k] = r[j];
                j++;
            }
        }
    }
}