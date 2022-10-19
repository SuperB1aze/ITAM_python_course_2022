list = input().split()
for i in range(len(list)):
    list[i] = int(list[i])
print(list[::2])