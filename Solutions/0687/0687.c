/***************************************************************************************************
 * Copyright: washing
 * FileName: 0687.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-9-2 10:31:57
***************************************************************************************************/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


int longestUnivaluePath(struct TreeNode* root){
    int ret = 0;
    int parse(struct TreeNode* root){
        int nls = 0, nrs = 0, tls = 0, trs = 0;
        if (root->left){
            nls = parse(root->left);
            if (root->val == root->left->val) tls = nls+1;
        }
        if (root->right){
            nrs = parse(root->right);
            if (root->val == root->right->val) trs = nrs+1;
        }
        ret = ret > tls+trs ? ret : trs+tls;
        return tls > trs ? tls : trs;
    }
    if (root) parse(root);
    return ret;
}
