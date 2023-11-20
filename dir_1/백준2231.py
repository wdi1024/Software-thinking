N = int(input())

for i in range(1, N+1):
    num = 0
    for j in range(len(str(i))):
        num += int((str(i)[j]))
    num += i
    if num == N:
        print(i)
        break

else: print(0)