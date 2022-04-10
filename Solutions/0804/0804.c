/***************************************************************************************************
 * Copyright: washing
 * FileName: 0804.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-4-10 11:28:21
***************************************************************************************************/

int uniqueMorseRepresentations(char ** words, int wordsSize){
    char dict[26][5] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
    char mores[100][60] = {0};
    int count = 0;
    for (int i=0; i<wordsSize; i++){
        char tmp[60] = { 0 };
        int flag = 0;
        for (int j=0; j<strlen(words[i]); j++){
            strcat(tmp, dict[words[i][j] - 'a']);
        }
        for (int k=0; k<count; k++){
            if (strcmp(mores[k], tmp) == 0){
                flag = 1;
                break;
            }
        }
        if (flag == 0){
            strcpy(mores[count], tmp);
            count++;
        }
    }
    return count;
}
