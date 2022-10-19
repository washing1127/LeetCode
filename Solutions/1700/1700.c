/***************************************************************************************************
 * Copyright: washing
 * FileName: 1700.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-10-19 10:38:35
***************************************************************************************************/

int countStudents(int* students, int studentsSize, int* sandwiches, int sandwichesSize){
    for (int i=0; i<sandwichesSize; i++) {
        int j=0;
        bool ok=false;
        for (; j<studentsSize; j++) {
            if (sandwiches[i] == students[j]) {
                students[j] = 2;
                ok = true;
                break;
            }
        }
        if (!ok) return studentsSize - i;
    }
    return 0;
}
