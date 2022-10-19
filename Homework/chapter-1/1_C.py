list = input().split()
k = 1
for i in range(len(list)):
    list[i] = int(list[i])
for i in range(len(list) - 1):
    if list[i] != list[i+1]:
        k +=1
        i +=1
print(k)