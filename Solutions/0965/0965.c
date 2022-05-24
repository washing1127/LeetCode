/***************************************************************************************************
 * Copyright: washing
 * FileName: 0965.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-5-24 11:42:48
***************************************************************************************************/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


bool isUnivalTree(struct TreeNode* root){
    int v = root->val;
    bool ret = true;
    void parse(struct TreeNode* root) {
        if (root->val != v) ret=false;
        if (ret && root->left) parse(root->left);
        if (ret && root->right) parse(root->right);
    }
    parse(root);
    return ret;
}
