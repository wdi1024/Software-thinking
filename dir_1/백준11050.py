import sys
import math
N, K = map(int, sys.stdin.readline().split())

upper = int(math.factorial(N))//int(math.factorial(N-K))
lower = int(math.factorial(K))
print(upper//lower)