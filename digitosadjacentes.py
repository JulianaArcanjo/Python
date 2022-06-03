n = int(input())
cond = True

while cond:
    x1 = n%10
    x = n//10
    x2 = x%10
    if n <= 10:
        print('não')
        cond = False
    elif n > 10 and x1 == x2:
        print('sim')
        cond = False
    else:
        n = n//10