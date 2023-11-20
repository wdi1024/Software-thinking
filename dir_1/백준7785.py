n = int(input())
work = set()
for _ in range(n):
    a, b = map(str, input().split())
    if b == "enter":
        work.add(a)
    if b == "leave":
        work.remove(a)

work = sorted(list(work), reverse=True)
for i in work:
    print(i)
