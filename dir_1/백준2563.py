N = int(input())

white_board = [[0] * 100 for _ in range(100)]

for _ in range(N):
    a, b = map(int, input().split())

    for y in range(b, b+10):
        for x in range(a, a+10):
            white_board[y][x] = 1

count = 0

for y in range(100):
    for x in range(100):
        if white_board[y][x] == 1:
            count += 1

print(count)
