class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        l = list(expression)
        heap = list()
        for idx,i in enumerate(l):
            # print(i)
            if i == '|' or i == '&': 
                heap.append(i)
                l[idx] = ''
            elif i == ',':
                if heap[-1] == '|': l[idx] = ' or '
                else: l[idx] = ' and '
            elif i == ')':
                if heap: heap.pop()
            elif i == 't':
                l[idx] = 'True'
            elif i == 'f':
                l[idx] = 'False'
            elif i == '!':
                l[idx] = ' not '
                if idx+1 < len(l) and l[idx+1] == '(':
                    heap.append(' not ')
        
        # print(l)
        return eval(''.join(l))