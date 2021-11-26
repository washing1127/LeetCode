/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


struct TreeNode* searchBST(struct TreeNode* root, int val){
    struct TreeNode* cur = root;
    while (cur){
        if (cur->val == val) return cur;
        else if (cur->val < val) cur = cur->right;
        else cur=cur->left;
    }
    return cur;
}
