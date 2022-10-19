def levelcount(block, i):
        block -= i
        if (block - i <= 0):
            print(i)
        else:
            i += 1
            levelcount(block, i)

block = int(input())
i = 0
levelcount(block, i)