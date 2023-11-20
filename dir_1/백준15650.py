import sys
n, m = map(int, sys.stdin.readline().split())
list1 = []


def f():
    if len(list1) == m:
        print(' '.join(map(str, list1)))
        return

    if len(list1) == 0:
        start = 1
    else:
        start = list1[-1]+1

    for i in range(start, n + 1):
        if i in list1:
            continue
        list1.append(i)
        f()
        list1.pop()


f()
