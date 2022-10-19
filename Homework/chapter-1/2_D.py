a = input().split()

for i in range(len(a)):
    a[i] = int(a[i])

a = a[-1:] + a[:-1]
print(a)