n = int(input())
getnum = []
for i in range(n):
    k = int(input())
    if k == 0:
        getnum.pop()
    else:
        getnum.append(k)

    tmp = k

print(sum(getnum))
