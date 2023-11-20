N, M = map(int, input().split())

list1 = [i+1 for i in range(N)]
removed = []
position = 0

for i in range(N, 0, -1):
    position = (position + M - 1) % i
    removed.append(list1[position])
    list1.pop(position)

print("<", end="")
for i in removed[:N-1]:
    print(i, end=', ')
print("{0}>".format(removed[-1]))

'''
2 % 7 -> 2 [1, 2, 3, 4, 5, 6, 7]
4 % 6 -> 4 [1, 2, 4, 5, 6, 7]
6 % 5 -> 1 [1, 2, 4, 5, 7]
(1+2) % 4 -> 3 [1, 4, 5, 7]
(3+2) % 3 -> 2 [1, 4, 5]
(2+2) % 2 -> 0 [1, 4]
(0+2) % 1 -> 0 [4]
'''