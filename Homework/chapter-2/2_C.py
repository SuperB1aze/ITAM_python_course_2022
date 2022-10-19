def number_system(value, base):
    alph = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(65, 91):
        alph.append(chr(i))
    converted_num = []
    converted_num.append(alph[value % base])
    while value >= base:
        value = value // base
        converted_num.append(alph[value % base])
    converted_num = converted_num[::-1]
    stroke = ""
    for i in range(0, len(converted_num)):
        stroke += converted_num[i]
    print(stroke)

a = input().split()
number_system(int(a[0]), int(a[1]))