class Solution {
public:
    string findLongestWord(string s, vector<string>& dictionary) {
        int l;
        int n = std::end(dictionary)-std::begin(dictionary);
        vector<string> d2(dictionary);
        for(char c : s){
            for(int i=0; i<n; i++){
                if (d2[i] != "" && d2[i][0] == c) {
                    l = d2[i].length();
                    d2[i] = d2[i].substr(1,l);
                }
            }
        }
        string ret="";
        for(int i=0; i<n; i++){
            string a = dictionary[i];
            string b = d2[i];
            if (b == ""){
                if (a.length()>ret.length()) ret=a;
                if (a.length()==ret.length() && a<ret) ret = a;
            }
        }
        return ret;
    }
};
