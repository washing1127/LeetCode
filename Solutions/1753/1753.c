/***************************************************************************************************
 * Copyright: washing
 * FileName: 1753.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-12-21 10:13:07
***************************************************************************************************/


int maximumScore(int a, int b, int c){
    int temp;
    if (a>b){
        temp = a;
        a = b;
        b = temp;
    }
    if (a>c){
        temp = a;
        a = c;
        c = temp;
    }
    if (b>c){
        temp = b;
        b = c;
        c = temp;
    }
    if (c > a+b) return a+b;
    return (a+b+c)/2;
}
