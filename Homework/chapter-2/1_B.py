def summation(start, end):
    sum = 0
    if start <= end:
        for i in range(start, end + 1):
            sum += i
    else:
        for i in range(start, end - 1, -1):
            sum += i
    return sum

a = input().split()
print( summation(int(a[0]), int(a[1])) )