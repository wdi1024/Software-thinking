import sys

N = int(sys.stdin.readline())

had = list(map(int, sys.stdin.readline().split()))
card = {}
for i in had:
    if i not in card:
        card[i] = 0
    card[i] += 1

M = int(input())

check = list(map(int, sys.stdin.readline().split()))

for i in check:
    if i not in card:
        print(0, end=' ')
    else:
        print(card[i], end=' ')