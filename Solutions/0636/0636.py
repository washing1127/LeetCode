# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/7 10:11
# File: 0636.py
# Desc: CV


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        st = []
        for log in logs:
            idx, tp, timestamp = log.split(':')
            idx, timestamp = int(idx), int(timestamp)
            if tp[0] == 's':
                if st:
                    ans[st[-1][0]] += timestamp - st[-1][1]
                    st[-1][1] = timestamp
                st.append([idx, timestamp])
            else:
                i, t = st.pop()
                ans[i] += timestamp - t + 1
                if st:
                    st[-1][1] = timestamp + 1
        return ans

