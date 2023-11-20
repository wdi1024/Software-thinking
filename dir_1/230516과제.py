# vocabulary.txt의 모든 단어에 대해 n-gram vocabulary 만들기
n = int(input())
f = open("/Users/wondaein/Desktop/국민대/23-1학기/소프트웨어적사고/vocabulary.txt")

WordList = f.read().split()
Dict = {}
for j in WordList:
    if len(j) >= n:
        for i in range(len(j)-n):
            if j[i:i+n] not in Dict:
                Dict[j[i:i+n]] = 1
            else:
                Dict[j[i:i+n]] += 1


sort = sorted(Dict, key=lambda x: Dict[x], reverse=True)
for i in sort:
    print(i+":"+str(Dict[i])+',', end=' ')
