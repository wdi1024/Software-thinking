
import sys
cnt = 0


def hanoi(start, tmp, stop, n):
    global cnt
    if n == 1:
        cnt += 1
        print("{} : {} -> {}".format(n, start, stop))
    else:
        hanoi(start, stop, tmp, n - 1)  # n-1개의 원판을 중간으로 옮김
        cnt += 1
        print("{} : {} -> {}".format(n, start, stop))  # 마지막 원판을 목적지로 옮김
        hanoi(tmp, start, stop, n-1)  # 나머지 원판을 목적지로 옮김


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    if N <= 20:
        hanoi(1, 2, 3, N)
        print(cnt)
