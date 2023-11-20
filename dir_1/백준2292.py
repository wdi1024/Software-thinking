N = int(input())

max_num = 1
floor = 1

while N > max_num:
    max_num += 6*floor
    floor += 1

print(floor)