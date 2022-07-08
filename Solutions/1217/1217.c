/***************************************************************************************************
 * Copyright: washing
 * FileName: 1217.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-7-8 10:55:33
***************************************************************************************************/


int minCostToMoveChips(int* position, int positionSize){
    int * c = (int *)malloc(sizeof(int) * positionSize*2);
    for (int i=0; i<positionSize*2; i++) c[i] = 0;
    for (int i=0; i<positionSize; i++){
        for (int j=0; j<positionSize*2; j+=2) {
            if (c[j] == position[i]) {
                c[j+1]++;
                break;
            } else if (c[j] == 0){
                c[j] = position[i];
                c[j+1] = 1;
                break;
            }
        }
    }
    int js = 0;
    int os = 0;
    for (int i=0; i < positionSize*2; i+=2) {
        if (c[i] % 2 == 0) os += c[i+1];
        else js += c[i+1];
    }
    return js < os ? js : os;
}
