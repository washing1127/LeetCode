/***************************************************************************************************
 * Copyright: washing
 * FileName: 2319.c
 * Author: washing
 * Version: 1.0
 * Date: 2023-01-31 10:26:53 
***************************************************************************************************/


bool checkXMatrix(int** grid, int gridSize, int* gridColSize){
    for (int i=0; i<gridSize; i++) {
        for (int j=0; j<gridSize; j++) {
            if (j == i | j == gridSize-1-i) {
                if (grid[i][j] == 0) return false;
            }
            else if (grid[i][j] != 0) {
                return false;
            }
        }
    }
    return true;
}
