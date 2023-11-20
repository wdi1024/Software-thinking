import sys
list1 = [int(sys.stdin.readline()) for _ in range(9)]
Sum = sum(list1)
x = 0
y = 0
for a in range(8):
    for b in range(a+1, 9):
        if Sum-list1[a]-list1[b] == 100:
            x = list1[a]
            y = list1[b]
list1.remove(x)
list1.remove(y)
list1 = sorted(list1)
for i in list1:
    print(i)
