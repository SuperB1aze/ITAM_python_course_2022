list = input()
for i in range(len(list)):
    if list[i].isupper():
        list = list[i:]
        break

k = 1
numcheck = False

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
for i in range(1, len(list)):
    for j in range(len(numbers)):
        if list[i] == numbers[j]:
            numcheck = True
            break
    if numcheck:
        k += 1
        break
    else:
        k += 1

list = list[::k]

for i in range(len(list)):
    if list[i] == '.':
        list = list[:i + 1]
        break

print(list)