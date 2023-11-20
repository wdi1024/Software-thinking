N = int(input())
k = []
for i in range(N):
    k.append(list(map(int, input().split())))

k.sort(key=lambda x: (x[1], x[0]))
count = 1
end_time = k[0][1]

for i in range(1, N):
    if k[i][0] >= end_time:
        count += 1
        end_time = k[i][1]

print(count)
