import sys
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0:
        break

    if max(a, b, c)**2 == a**2+b**2+c**2-max(a, b, c)**2:
        print('right')
    else:
        print('wrong')
