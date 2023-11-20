from operator import itemgetter
N = int(input())
dic = []
for i in range(N):
    a, b = map(str, input().split())
    dic.append([int(a), b, i])

dic.sort(key=itemgetter(0, 2))
for i in dic:
    print(i[0], i[1])
