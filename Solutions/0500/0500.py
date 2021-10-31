class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a = {'q','w','e','r','t','y','u','i','o','p'}
        b = {'a','s','d','f','g','h','j','k','l'}
        c = {'z','x','c','v','b','n','m'}
        ret = []
        for i in words:
            for s in [a, b, c]:
                flag = True
                for l in set(i):
                    if l.lower() not in s:
                        flag = False
                if flag: 
                    ret.append(i)
                    break
        return ret
