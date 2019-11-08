N = int(input())
list = []

for i in range(N):
    if i<2:
        list.append(i)
    else:
        list.append(list[i-2] + list[i-1])
print(*list, sep = ',')
