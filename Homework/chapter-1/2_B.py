num = int(input())
a = []
offline = 0; online = 0; unknown = 0
boolcheck = 0

for i in range(num):
    a.append([])
    a[i] = input().split()

for i in range(num):
    for j in range(4):
        if a[i][j] == 'True':
            a[i][j] = True
        elif a[i][j] == 'False':
            a[i][j] = False

for i in range(num):
    for j in range(4):
        if isinstance(a[i][j], bool):
            boolcheck += 1

    if boolcheck == 0:
        unknown += 1
    elif boolcheck == 1:
        for g in range(4):
            if isinstance(a[i][g], bool):
                temp = g
                break
        if a[i][temp]:
            online += 1
        elif not a[i][temp]:
            offline += 1
    else:
        if not isinstance(a[i][3], bool):
            unknown += 1
        else:
            if a[i][3]:
                online += 1
            elif not a[i][3]:
                offline += 1
    boolcheck = 0
print(online, offline, unknown)