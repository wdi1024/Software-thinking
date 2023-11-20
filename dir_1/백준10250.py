import sys
t = int(input())
for i in range(t):
    H, W, N = map(int, sys.stdin.readline().split())
    floor = N % H
    num = N//H+1

    if N%H==0:
        floor = H
        num = N//H


    print(floor*100+num)