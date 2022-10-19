num = int(input())
a = []
offline = 0
online = 0
for i in range(num):
    a.append([])
    a[i] = input().split()

for i in range(num):
    if a[i][3] == 'True':
        a[i][3] = 1
    else:
        a[i][3] = 0

    if a[i][3]:
        online += 1
    elif not a[i][3]:
        offline += 1
print(online, offline)