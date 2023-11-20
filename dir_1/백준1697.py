from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())
visited = [987654321 for _ in range(100001)]
que = deque()

visited[N] = 0
que.append([N, 0])
while que:
    front = que.popleft()
    now_X, now_T = front[0], front[1]

    if now_X+1 <= 100000 and visited[now_X+1] > now_T+1:
        visited[now_X + 1] = now_T + 1
        que.append([now_X+1, now_T+1])
    if now_X-1 >= 0 and visited[now_X-1] > now_T+1:
        visited[now_X-1] = now_T+1
        que.append([now_X-1, now_T+1])
    if now_X*2 <= 100000 and visited[now_X*2] > now_T+1:
        visited[now_X*2] = now_T+1
        que.append([now_X*2, now_T+1])

print(visited[K])