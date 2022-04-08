/***************************************************************************************************
 * Copyright: washing
 * FileName: 0429.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-4-8 10:49:53
***************************************************************************************************/

/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     int numChildren;
 *     struct Node** children;
 * };
 */

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
# define MAX_LEVE_SIZE 1000
# define MAX_NODE_SIZE 10000

int** levelOrder(struct Node* root, int* returnSize, int** returnColumnSizes) {
    int ** ret = (int **)malloc(sizeof(int *) * MAX_LEVE_SIZE);
    *returnColumnSizes = (int *)malloc(sizeof(int) * MAX_LEVE_SIZE);
    if (!root){
        *returnSize = 0;
        return ret;
    }
    struct Node ** queue = (struct Node **)malloc(sizeof(struct Node *) * MAX_NODE_SIZE);
    int head = 0, tail = 0;
    int level = 0;
    queue[tail++] = root;
    while (head != tail){
        int cnt = tail - head;
        ret[level] = (int *)malloc(sizeof(int) * cnt);
        for(int i=0; i<cnt; i++){
            struct Node * cur = queue[head++];
            ret[level][i] = cur->val;
            for(int j=0; j<cur->numChildren; j++){
                queue[tail++] = cur->children[j];
            }
        }
        (*returnColumnSizes)[level++] = cnt;
    }
    *returnSize = level;
    free(queue);
    return ret;
}
