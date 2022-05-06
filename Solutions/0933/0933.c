/***************************************************************************************************
 * Copyright: washing
 * FileName: 0933.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-5-6 10:11:42
***************************************************************************************************/

typedef struct {
    int *queue;
    int capability;
    int head;
    int tail;
} RecentCounter;


RecentCounter* recentCounterCreate() {
    RecentCounter *obj = (RecentCounter *)malloc(sizeof(RecentCounter));
    obj->capability = 10001;
    obj->queue = (int *)malloc(sizeof(int) * obj->capability);
    obj->head = 0;
    obj->tail = 0;
    return obj;
}

int recentCounterPing(RecentCounter* obj, int t) {
    obj->queue[obj->tail++] = t;
    while (obj->queue[obj->head] < t - 3000) obj->head++;
    return obj->tail - obj->head;
}

void recentCounterFree(RecentCounter* obj) {
    free(obj->queue);
    free(obj);
}

/**
 * Your RecentCounter struct will be instantiated and called as such:
 * RecentCounter* obj = recentCounterCreate();
 * int param_1 = recentCounterPing(obj, t);

 * recentCounterFree(obj);
*
