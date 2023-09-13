lst = [1, 2, 3, 4, 5, 6, 7]
ck1, ck2 = 0, 0
for i in lst:
    if ck1 == 0 and i%2 == 1:
        print(i, end = ' ')
        ck1 = 1
    if ck2 == 0 and i%2 == 0:
        print(i, end = ' ')
        ck2 = 1
        