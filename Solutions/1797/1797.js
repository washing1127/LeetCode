// Author: washing
// DateTime: 2023/2/9 10:42
// File: 1797.js
// Desc: 


var AuthenticationManager = function(timeToLive) {
    this.timeToLive = timeToLive;
    this.map = new Map();
};

AuthenticationManager.prototype.generate = function(tokenId, currentTime) {
    this.map.set(tokenId, currentTime + this.timeToLive);
};

AuthenticationManager.prototype.renew = function(tokenId, currentTime) {
    if ((this.map.get(tokenId) || 0) > currentTime) {
        this.map.set(tokenId, currentTime + this.timeToLive);
    }
};

AuthenticationManager.prototype.countUnexpiredTokens = function(currentTime) {
    let res = 0;
    for (const time of this.map.values()) {
        if (time > currentTime) {
            res++;
        }
    }
    return res;
};

// 作者：力扣官方题解
// 链接：https://leetcode.cn/problems/design-authentication-manager/solutions/2099432/she-ji-yi-ge-yan-zheng-xi-tong-by-leetco-kqqb/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
