/***************************************************************************************************
 * Copyright: washing
 * FileName: 1779.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-12-01 13:49:43
***************************************************************************************************/

int nearestValidPoint(int x, int y, int** points, int pointsSize, int* pointsColSize){
    int ret = -1;
    int min = 10000;
    for (int idx=0; idx<pointsSize; idx++){
        int _x = points[idx][0], _y = points[idx][1];
        if (_x == x) {
            int cha = _y>y ? _y-y : y-_y;
            if (cha == 0) return idx;
            if (cha < min){
                ret = idx;
                min = cha;
            }
        }else if (_y == y) {
            int cha = _x>x ? _x-x : x-_x;
            if (cha == 0) return idx;
            if (cha < min){
                ret = idx;
                min = cha;
            }
        }
    }
    return ret;
}
