/***************************************************************************************************
 * Copyright: washing
 * FileName: 0824.c
 * Author: washing
 * Version: 1.0
 * Date: 2022-4-21 13:47:08
***************************************************************************************************/

bool isyy(char c){
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
}

char * toGoatLatin(char * sentence){
    int num_of_words = 1;
    for (int i=0; i<strlen(sentence); i++) {
        if (sentence[i] == ' ') num_of_words += 1;
    }
    int ret_len = strlen(sentence);
    ret_len += num_of_words*2;
    ret_len += (num_of_words+1)*num_of_words/2;
    char * ret = (char *)malloc(sizeof(char) * (ret_len+1));
    bool new_word = true;
    char temp = 'a';
    int ret_idx = 0;
    int word_count = 1;
    for (int i=0; i<strlen(sentence); i++){
        char this = sentence[i];
        if (new_word) {
            new_word = false;
            if (!isyy(this)) {
                temp = this;
            } else {
                ret[ret_idx++] = this;
            }
        } else {
            if (this == ' ') {
                new_word = true;
                if (temp != 'a') {
                    ret[ret_idx++] = temp;
                    temp = 'a';
                }
                ret[ret_idx++] = 'm';
                ret[ret_idx++] = 'a';
                for (int _=0; _<word_count; _++) ret[ret_idx++] = 'a';
                word_count++;
                ret[ret_idx++] = ' ';
            } else {
                new_word = false;
                ret[ret_idx++] = this;
            }
        }
    }
    if (temp != 'a') {
        ret[ret_idx++] = temp;
    }
    ret[ret_idx++] = 'm';
    ret[ret_idx++] = 'a';
    for (int _=0; _<word_count; _++) ret[ret_idx++] = 'a';
    ret[ret_len] = '\0';
    return ret;
}
