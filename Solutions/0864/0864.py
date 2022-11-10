# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/10 18:11
# File: 0864.py
# Desc: CV


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        m, n = len(grid), len(grid[0])
        sx = sy = 0
        key_to_idx = dict()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    sx, sy = i, j
                elif grid[i][j].islower():
                    if grid[i][j] not in key_to_idx:
                        idx = len(key_to_idx)
                        key_to_idx[grid[i][j]] = idx

        q = deque([(sx, sy, 0)])
        dist = dict()
        dist[(sx, sy, 0)] = 0
        while q:
            x, y, mask = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != "#":
                    if grid[nx][ny] == "." or grid[nx][ny] == "@":
                        if (nx, ny, mask) not in dist:
                            dist[(nx, ny, mask)] = dist[(x, y, mask)] + 1
                            q.append((nx, ny, mask))
                    elif grid[nx][ny].islower():
                        idx = key_to_idx[grid[nx][ny]]
                        if (nx, ny, mask | (1 << idx)) not in dist:
                            dist[(nx, ny, mask | (1 << idx))] = dist[(x, y, mask)] + 1
                            if (mask | (1 << idx)) == (1 << len(key_to_idx)) - 1:
                                return dist[(nx, ny, mask | (1 << idx))]
                            q.append((nx, ny, mask | (1 << idx)))
                    else:
                        idx = key_to_idx[grid[nx][ny].lower()]
                        if (mask & (1 << idx)) and (nx, ny, mask) not in dist:
                            dist[(nx, ny, mask)] = dist[(x, y, mask)] + 1
                            q.append((nx, ny, mask))
        return -1

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/shortest-path-to-get-all-keys/solutions/1959739/huo-qu-suo-you-yao-chi-de-zui-duan-lu-ji-uu5m/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
