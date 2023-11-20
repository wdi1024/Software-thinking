N = int(input())
answer = []
for i in range(N):
    stri = input()
    stack = []
    for a in stri:
        if a == '(':
            stack.append(a)
        else:
            if stack:
                if stack[-1] == '(':
                    stack.pop()
            else:
                stack.append(a)
                continue

    if stack:
        answer.append('NO')
    else:
        answer.append('YES')

for b in answer:
    print(b)
