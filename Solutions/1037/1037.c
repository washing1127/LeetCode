/***************************************************************************************************
 * Copyright: washing
 * FileName: 1037.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-6-8 10:55:59
***************************************************************************************************/

bool isBoomerang(int** points, int pointsSize, int* pointsColSize){
    int x1=points[0][0], x2=points[1][0], x3=points[2][0], y1=points[0][1], y2=points[1][1], y3=points[2][1];
    return (x2-x1)*(y3-y1) != (x3-x1)*(y2-y1);
}
