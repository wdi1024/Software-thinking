k = []
answer = []
a = int(input())
while a != 0:
    k.append(a)
    a = int(input())

for i in k:
    i = str(i)
    if i == i[::-1]:
        answer.append('yes')
    else:
        answer.append('no')
for i in answer:
    print(i)
