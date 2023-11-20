N = int(input())
students = []
for _ in range(N):
    students.append(list(map(int, input().split())))

ranks = []
for student in students:
    rank = 1

    for other in students:
        if student == other:
            continue

        if student[0] < other[0] and student[1] < other[1]:
            rank += 1

    ranks.append(rank)

for i in range(len(ranks)):
    print(ranks[i], end=' ')
