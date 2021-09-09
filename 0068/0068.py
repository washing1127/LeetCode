class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def deal_subs(subs, maxWidth):
            space_num = subs.count(" ")
            if space_num == 0:
                return subs+" "*(maxWidth-len(subs))
            mw = maxWidth - len(subs) + space_num
            less_space = mw//space_num
            more_space_num = mw%space_num
            subs = subs.replace(" ", " "*less_space).replace(" "*less_space, " "*(less_space+1),more_space_num)
            return subs

        ret = []
        subs = words[0]
        for word in words[1:]:
            if len(subs) + len(word) + 1 > maxWidth:
                ret.append(deal_subs(subs, maxWidth))
                subs = word
            else:
                subs += " " + word
        ret.append(subs+" "*(maxWidth-len(subs)))
        return ret
