// Author: washing
// DateTime: 2021/9/2 18:50
// File: Offer22.cpp
// Desc: 


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* getKthFromEnd(ListNode* head, int k) {
        int n = 1;
        ListNode* cur = head;
        while (cur->next != NULL){
            cur = cur->next;
            n++;
        }
        cur = head;
        for (int i=1; i<=n; i++){
            if (i > n-k) break;
            cur = cur -> next;
        }
        return cur;
    }
};