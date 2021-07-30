// Author: washing
// DateTime: 2021/7/30 11:16
// File: 0171.js
// Desc: 


/**
 * @param {string} columnTitle
 * @return {number}
 */
var titleToNumber = function(columnTitle) {
    var n = 0;
    var i;
    for (var idx=0; idx < columnTitle.length; idx++){
        i = columnTitle[idx];
        n = n*26 + i.charCodeAt() - 64;
    }
    return n;
};