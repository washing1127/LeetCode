/***************************************************************************************************
 * Copyright: washing
 * FileName: 1672.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-4-14 13:20:03
***************************************************************************************************/

int maximumWealth(int** accounts, int accountsSize, int* accountsColSize){
    int ret = 0;
    for(int i=0; i<accountsSize; i++){
        int total = 0;
        for(int j=0; j<*accountsColSize; j++){
            total+=accounts[i][j];
        }
        ret = total>ret ? total : ret;
    }
    return ret;
}
