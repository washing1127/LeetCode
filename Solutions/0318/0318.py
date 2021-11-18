class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dic = dict()
        for word in words:
            l = ['0']*26
            for c in word:
                l[ord(c)-97] = '1'
            s = '0b'+''.join(l)
            dic[word] = [len(word), int(s,2)]
        ret = 0
        n = len(words)
        for i in range(n-1):
            l1, v1 = dic[words[i]]
            for j in range(i+1,n):
                l2, v2 = dic[words[j]]
                if v2 & v1 == 0:
                    ret = max(l1*l2, ret)
        return ret
