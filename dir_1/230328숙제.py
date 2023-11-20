a, b, c = map(int, input().split())
n = 0
for i in range(1, a):
    if (i % 400 == 0) | (i % 4 == 0 and i % 100 != 0):
        n += 366
    else:
        n += 365

if a % 400 == 0 | (a % 4 == 0 and a % 100 != 0):
    k = 2
else:
    k = 1

month1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(b-1):
    if k == 1:
        n += month1[i]
    else:
        n += month2[i]

n += c
'''
if b == 1:
    n += c
elif b == 2:
    n += (c+31)
elif b == 3:
    n += (c+31)
    if k == 2:
        n += 29
    else:
        n += 28
elif b == 4:
    n += (c+62)
    if k == 2:
        n += 29
    else:
        n += 28
elif b == 5:
    n += (c+92)
    if k == 2:
        n += 29
    else:
        n += 28
elif b == 6:
    n += (c+123)
    if k == 2:
        n += 29
    else:
        n += 28
elif b == 7:
    n += (c+153)
    if k == 2:
        n += 29
    else:
        n += 28
elif b == 8:
    n += (c+184)
    if k == 2:
        n += 29
    else:
        n += 28
elif b == 9:
    n += (c+215)
    if k == 2:
        n += 29
    else:
        n += 28
elif b == 10:
    n += (c+245)
    if k == 2:
        n += 29
    else:
        n += 28
elif b == 11:
    n += (c+276)
    if k == 2:
        n += 29
    else:
        n += 28
else:
    n += (c + 306)
    if k == 2:
        n += 29
    else:
        n += 28


if n % 7 == 1:
    print('월요일')
elif n % 7 == 2:
    print('화요일')
elif n % 7 == 3:
    print('수요일')
elif n % 7 == 4:
    print('목요일')
elif n % 7 == 5:
    print('금요일')
elif n % 7 == 6:
    print('토요일')
else:
    print('일요일')
'''

week = ["일요일", '월요일', '화요일', '수요일', '목요일', '금요일', '토요일']

print(week[n % 7])
