n = int(input())
an = n
data = []
if n % 5 == 0:
    print(n // 5)
else:
    cnt = 0
    while an > 5:
        an -= 5
        cnt += 1
        if an % 3 == 0:
            data.append(cnt+(an//3))
    if data:
        print(min(data))
    else:
        if n % 3 == 0:
            print(n//3)
        else:
            print(-1)