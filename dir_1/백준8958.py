N=int(input())
i=0
answer=[]
while N>i:
    str=input()
    score=0
    time=1
    for a in str:
        if a == 'O':
            score += time
            time += 1
        else:
            time = 1
    answer.append(score)
    i += 1
for k in answer:
    print(k)