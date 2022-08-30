/***************************************************************************************************
 * Copyright: washing
 * FileName: 0998.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-8-30 15:23:03
***************************************************************************************************/



/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


struct TreeNode* insertIntoMaxTree(struct TreeNode* root, int val){
    struct TreeNode* t = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    t->val = val;
    t->left = NULL;
    t->right = NULL;
    if (root->val < val) {
        t->left = root;
        return t;
    }
    struct TreeNode* cur = root;
    while (cur) {
        if (!cur->right) {
            cur->right = t;
            break;
        } else if (cur->right->val < val) {
            t->left = cur->right;
            cur->right = t;
            break;
        }
        cur = cur->right;
    }
    return root;
}
