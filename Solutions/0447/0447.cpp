class Solution {
public:
    int numberOfBoomerangs(vector<vector<int>>& points) {
        int ret=0;
        for (auto &p1 : points){
            std::map<int, int> dic;
            for (auto &p2 : points){
                int dis = (p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1]);
                dic[dis]++;
            }
            for (auto &[k, v]: dic){
                ret += v*(v-1);
            }
        }
        return ret;
    }
};
