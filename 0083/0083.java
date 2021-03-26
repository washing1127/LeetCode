// Author: washing
// DateTime: 2021/3/26 11:59
// File: 0083.java
// Desc: 

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) 
            return head;
        int num = head.val;
        ListNode ret = new ListNode(num);
        ListNode cur = ret;
        while (head.next != null){
            head = head.next;
            int v = head.val;
            if (num != v){
                num = v;
                cur.next = new ListNode(num);
                cur = cur.next;
            }
        }
        return ret;
    }
}