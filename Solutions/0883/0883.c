/***************************************************************************************************
 * Copyright: washing
 * FileName: 0883.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-4-26 10:50:19
***************************************************************************************************/

int projectionArea(int** grid, int gridSize, int* gridColSize){
    int ret = 0;
    int temp[gridSize];
    for (int i=0; i<gridSize; i++) temp[i] = 0;
    for (int i=0; i<gridSize; i++) {
        int colmax = 0;
        for (int j=0; j<gridSize; j++) {
            if (grid[i][j] != 0) ret++;
            colmax = fmax(grid[i][j], colmax);
            temp[j] = fmax(grid[i][j], temp[j]);
        }
        ret += colmax;
    }
    for (int i=0; i<gridSize; i++) ret += temp[i];
    return ret;
}
