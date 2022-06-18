from collections import deque


def bfs(graph, checked):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque([[0, 0, 0]])
    checked[0][0][0] = 1

    while queue:
        x, y, wall = queue.popleft()
        if x == n - 1 and y == m - 1:
            return checked[x][y][wall]

        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]

            # 1. 범위를 벗아나지 않는 좌표이다.  2. 미방문인 좌표이다.
            if 0 <= ax < n and m > ay >= 0 == checked[ax][ay][wall]:

                # 벽이 아닌 좌표이다.
                if graph[ax][ay] == '0':
                    queue.append([ax, ay, wall])
                    checked[ax][ay][wall] = checked[x][y][wall] + 1

                # 1. 벽을 부신 전적이 없다. 2. 다음 이동할 좌표가 벽이다.
                if wall == 0 and graph[ax][ay] == '1':
                    queue.append([ax, ay, 1])
                    checked[ax][ay][1] = checked[x][y][wall] + 1
    return -1


n, m = map(int, input().split())
grahp = [list(input()) for _ in range(n)]
checked = [[[0, 0] for _ in range(m)] for _ in range(n)]

print(bfs(grahp, checked))