/***************************************************************************************************
 * Copyright: washing
 * FileName: 0819.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-4-17 11:25:00
***************************************************************************************************/

char isalphat(char c){
    if (c>=97 && c<=122) return c;
    else if (c>=65 && c<=90) return c+32;
    return 0;
}

char * mostCommonWord(char * paragraph, char ** banned, int bannedSize){
    char *tmp, c;
    short i, len=strlen(paragraph), j;
    short table[512] = {0}, start, end, maxtime=0;
    unsigned long int key = 0;
    for(bannedSize--;bannedSize>=0;bannedSize--){
        for(key=0,i=0;(c=banned[bannedSize][i])!='\0';i++){
            key = (key << 5) - key + c - 97;
        }
        key = (key&511);
        table[key] = -1;
    }
    for(i=0;i<len;i++){
        if((i==0||paragraph[i-1]==' ')&&paragraph[i]!=' '){
            for(j=i,key=0;(c=isalphat(paragraph[i]))!=0;i++){
                key = (key << 5) - key + c - 97;
            }
            key = key&511;
            if(table[key]!=-1){
                table[key]++;
                if(table[key]>maxtime){
                    maxtime=table[key];
                    start = j;
                    end = i;
                }
            }
        }
    }
    tmp=(char *)malloc((end-start+1)*sizeof(char));
    for(j=0;start<end;j++,start++) tmp[j] = isalphat(paragraph[start]);
    tmp[j] = '\0';
    return tmp;
}
