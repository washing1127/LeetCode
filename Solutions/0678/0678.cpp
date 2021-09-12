class Solution {
public:
    bool checkValidString(string s) {
        stack <int>l;
        stack <int>x;
        int n = std::end(s) - std::begin(s);
        for (int i=0;i<n;i++){
            if (s[i] == '(') l.push(i);
            if (s[i] == '*') x.push(i);
            if (s[i] == ')'){
                if (l.size()>0) l.pop();
                else if (x.size()>0) x.pop();
                else return false;
            }
        }
        while (l.size()){
            if (x.empty()) return false;
            if (l.top() < x.top()) {
                l.pop();
                x.pop();
            }else return false;
        }
        return true;
    }
};
