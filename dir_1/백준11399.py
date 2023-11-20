N = int(input())

cust = list(map(int, input().split()))
answer = []
while cust:
    min = cust[0]
    for i in cust:
        if min >= i:
            min = i
    answer.append(min)
    cust.remove(min)
sum=0
for i in range(len(answer)):
    sum += (answer[i]*(len(answer)-i))
print(sum)