// Author: washing
// DateTime: 2023/2/10 18:42
// File: 1223.js
// Desc: 


const MOD = 1000000007;
var dieSimulator = function(n, rollMax) {
    const d = new Array(n + 1).fill(0).map(() => new Array(6).fill(0).map(() => new Array(16).fill(0)));
    for (let j = 0; j < 6; j++) {
        d[1][j][1] = 1;
    }
    for (let i = 2; i <= n; i++) {
        for (let j = 0; j < 6; j++) {
            for (let k = 1; k <= rollMax[j]; k++) {
                for (let p = 0; p < 6; p++) {
                    if (p !== j) {
                        d[i][p][1] = (d[i][p][1] + d[i - 1][j][k]) % MOD;
                    } else if (k + 1 <= rollMax[j]) {
                        d[i][p][k + 1] = (d[i][p][k + 1] + d[i - 1][j][k]) % MOD;
                    }
                }
            }
        }
    }

    let res = 0;
    for (let j = 0; j < 6; j++) {
        for (let k = 1; k <= rollMax[j]; k++) {
            res = (res + d[n][j][k]) % MOD;
        }
    }
    return res;
};

// 作者：力扣官方题解
// 链接：https://leetcode.cn/problems/dice-roll-simulation/solutions/2102282/zhi-tou-zi-mo-ni-by-leetcode-solution-yg0s/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
