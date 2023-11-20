import sys
n, m = map(int, sys.stdin.readline().split())
list1 = []


def f(k):
    if len(list1) == m:
        for j in list1:
            print(j, end=' ')
        print()
        return

    for i in range(k, n + 1):
        if len(list1) > 0:
            if list1[-1] > i:
                continue
        list1.append(i)
        f(k)
        list1.pop()


f(1)
