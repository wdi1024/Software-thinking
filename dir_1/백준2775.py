N = int(input())
while N > 0:
    k = int(input())
    n = int(input())
    floor = []
    zero = [i for i in range(1, n+1)]
    floor.append(zero)

    for i in range(1, k+1):
        list1 = []
        for j in range(n):
            tmp = 0
            for l in range(j+1):
                tmp += floor[i-1][l]
            list1.append(tmp)
        floor.append(list1)

    print(floor[k][n-1])
    N -= 1

