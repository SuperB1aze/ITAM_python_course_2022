def summation(*args):
    a = [i for i in args]
    sum = 0
    max = a[0]
    for i in range(len(a)):
        if a[i] < 0:
            a[i] *= -2
        if a[i] > max:
            max = a[i]
        sum += a[i]
    print(sum / max)

summation(-10, 2, 3, 15, -4)