int findLongestNode(int u, int * parent, const struct ListNode ** adj, int n) {
    int * queue = (int *)malloc(sizeof(int) * n);
    int head = 0, tail = 0;
    bool * visit = (bool *)malloc(sizeof(bool) * n);
    memset(visit, 0, sizeof(bool) * n);
    queue[tail++] = u;
    visit[u] = true;
    int res = -1;

    while (head != tail) {
        int curr = queue[head++];
        res = curr;
        struct ListNode * node = adj[curr];
        while (node) {
            if (!visit[node->val]) {
                visit[node->val] = true;
                parent[node->val] = curr;
                queue[tail++] = node->val;
            }
            node = node->next;
        }
    }
    free(queue);
    free(visit);
    return res;
}

int* findMinHeightTrees(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize){
    int * res = NULL;
    if (n == 1) {
        res = (int *)malloc(sizeof(int));
        *res = 0;
        *returnSize = 1;
        return res;
    }

    struct ListNode ** adj = (struct ListNode *)malloc(sizeof(struct ListNode *) * n);
    for (int i = 0; i < n; i++) {
        adj[i] = NULL;
    }
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0];
        int v = edges[i][1];
        struct ListNode * node = (struct ListNode *)malloc(sizeof(struct ListNode));
        node->val = u;
        node->next = adj[v];
        adj[v] = node;
        node = (struct ListNode *)malloc(sizeof(struct ListNode));
        node->val = v;
        node->next = adj[u];
        adj[u] = node;
    }
    
    int * parent = (int *)malloc(sizeof(int) * n);
    /* 找到与节点 0 最远的节点 x */
    int x = findLongestNode(0, parent, adj, n);
    /* 找到与节点 x 最远的节点 y */
    int y = findLongestNode(x, parent, adj, n);
    /* 求出节点 x 到节点 y 的路径 */
    int * path = (int *)malloc(sizeof(int) * n);
    int pos = 0;
    parent[x] = -1;
    while (y != -1) {
        path[pos++] = y;
        y = parent[y];
    }
    if (pos % 2 == 0) {
        res = (int *)malloc(sizeof(int) * 2);
        res[0] = path[pos / 2 - 1];
        res[1] = path[pos / 2];
        *returnSize = 2;
    } else {
        res = (int *)malloc(sizeof(int));
        *res = path[pos / 2];
        *returnSize = 1;
    }
    free(path);
    free(parent);
    for (int i = 0; i < n; i++) {
        struct ListNode * node = adj[i];
        while (node) {
            struct ListNode * curr = node;
            node = curr->next;
            free(curr);
        }
    }
    free(adj);
    return res;
}

