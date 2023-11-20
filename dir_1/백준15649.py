import sys
n, m = map(int, sys.stdin.readline().split())
list1 = []


def f():
    if len(list1) == m:
        print(' '.join(map(str, list1)))
        return

    for i in range(1, n + 1):
        if i in list1:
            continue

        list1.append(i)
        f()
        list1.pop()


f()