/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        int n=0;
        ListNode *cur = head;
        while (cur){
            n++;
            cur = cur -> next;
        }
        int num = n/k, ys = n%k;
        vector<ListNode*> ret(k, nullptr);
        cur = head;
        for(int i=0; i<k && cur; i++){
            ret[i] = cur;
            int plus = num + (i < ys ? 1 : 0);
            for (int j=1; j<plus; j++) cur = cur -> next;
            ListNode *next = cur -> next;
            cur -> next = nullptr;
            cur = next;
        }
        return ret;
    }
};
