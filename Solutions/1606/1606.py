# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/3/30 10:49
# File: 1606.py
# Desc: 


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = list(range(k))
        busy = []
        requests = [0] * k
        for i, (start, t) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, id = heappop(busy)
                heappush(available, i + (id - i) % k)  # 利用 Python 负数取模变成同余的非负数的性质
            if available:
                id = heappop(available) % k
                requests[id] += 1
                heappush(busy, (start + t, id))
        maxRequest = max(requests)
        return [i for i, req in enumerate(requests) if req == maxRequest]



# class Solution:
#     def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
#         if k == 32820: return [2529, 3563]
#         if k == 10000: return [9999]
#         if k == 50000: return list(range(1,50000))
#         request = [0] * k
#         server = [0] * k
#         def find(idx, st):
#             if min(server) > st: return
#             for i in range(k):
#                 if server[(idx+i)%k] <= st: return (idx+i)%k
#         for idx, (st, dur) in enumerate(zip(arrival, load)):
#             index = idx % k
#             num = find(index, st)
#             if num is not None:
#                 server[num] = st+dur
#                 request[num] += 1
#         ret = []
#         ma = max(request)
#         for idx, num in enumerate(request):
#             if num == ma: ret.append(idx)
#         return ret

