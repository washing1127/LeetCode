
bool canConstruct(char * ransomNote, char * magazine){
    for (int i=0; i<strlen(ransomNote); i++){
        bool flag = false;
        for (int j=0;j<strlen(magazine); j++){
            if (ransomNote[i]==magazine[j]){
                magazine[j] = "O";
                flag = true;
                break;
            }
        }
        if (flag == false) return false;
    }
    return true;
}
