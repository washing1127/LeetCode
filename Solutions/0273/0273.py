DIC = {0:"",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety",}

class Solution:
    def numberToWords(self, num: int) -> str:
        if not num: return "Zero"
        def parse3(num):
            r = ''
            if num >= 100:
                r += DIC[num//100] + " Hundred "
                num %= 100
            if num in DIC.keys():
                return r + " " + DIC[num]
            if num >= 10:
                r += " " + DIC[num//10*10]
                num %= 10
            if num >= 0:
                r += " " + DIC[num]
            return r
        # 2,147,483,647
        # 1,234,567,891
        ret = ""
        if num >= 1000000000:
            s = num // 1000000000
            ret += DIC[s] + " Billion "
            num %= 1000000000
        if num >= 1000000:
            s = num // 1000000
            ret += parse3(s) + " Million "
            num %= 1000000
        if num >= 1000:
            s = num // 1000
            ret += parse3(s) + " Thousand "
            num %= 1000
        ret += parse3(num)
        while "  " in ret:
            ret = ret.replace("  ", " ")
        return ret.strip()
