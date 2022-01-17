class Solution:
    def countVowelPermutation(self, n: int) -> int:
        d1 = {"a":1,"e":1,"i":1,"o":1,"u":1}
        for i in range(1,n):
            ne = d1['a']
            ni = na = d1['e']
            nu = no = d1['i']
            na += no
            ne += no
            ni += d1['o']
            nu += d1['o']
            na += d1['u']
            d1['a'] = na
            d1['e'] = ne
            d1['i'] = ni
            d1['o'] = no
            d1['u'] = nu
        return sum(d1.values()) % (10 ** 9 + 7)
