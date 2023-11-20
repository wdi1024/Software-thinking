import sys

N = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))
d_M = list(set(M))
d_M.sort()

dic = dict()
for i in range(len(d_M)):
    dic[d_M[i]] = i

for i in M:
    print(dic[i], end=' ')