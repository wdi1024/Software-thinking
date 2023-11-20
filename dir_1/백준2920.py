k = list(map(int, input().split()))
sk=sorted(k)
rk=sorted(k,reverse=True)
if k == sk:
    print('ascending')
elif k == rk:
    print('descending')
else:
    print('mixed')