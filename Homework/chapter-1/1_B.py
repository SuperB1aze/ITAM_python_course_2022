from msvcrt import kbhit


list = input().split()
k = 0
for i in range(len(list)):
    list[i] = int(list[i])
for i in range(len(list)):
    if list[i] > 0:
        k+=1
print(k)