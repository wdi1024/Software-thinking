N = int(input())

fibo_list = [i for i in range(N+1)]
fibo_list[0] = 0
fibo_list[1] = 1

for i in range(2, N+1):
    fibo_list[i] = fibo_list[i-2]+fibo_list[i-1]

print(fibo_list[N])