# 시간 초과: O(N * M * 1000 * 1000)

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

graph = []
walls = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = 1e9

# graph
for i in range(n):
    graph.append([])
    string = input()

    for j in range(m):
        if string[j] == "1":
            walls.append([i, j])
        graph[i].append(string[j])

for wall in walls:
    graph[wall[0]][wall[1]] = '0'
    count = [[1e9] * m for i in range(n)]
    count[0][0] = 1

    queue = deque([[0, 0]])

    # BFS
    while queue:
        ver = queue.popleft()
        x, y = ver[0], ver[1]

        # 상하좌우
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]

            # 범위
            if 0 <= ax < n and 0 <= ay < m and graph[ax][ay] != '1':
                if count[x][y] + 1 < count[ax][ay] and count[x][y] + 1 < result:
                    count[ax][ay] = count[x][y] + 1
                    queue.append([ax, ay])

    graph[wall[0]][wall[1]] = '1'
    result = min(result, count[n-1][m-1])

if result == 1e9:
    print(-1)
else:
    print(result)