x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if x1 % 2 == 1 or x2 % 2 == 1:
    if y1 % 2 == 0 or y2 % 2 == 0:
        print('YES')
    elif y1 % 2 == 1 or y2 % 2 == 1:
        print('YES')
    else:
        print('NO')
elif y1 % 2 == 1 and y2 % 2 == 1:
        print('YES')
else:
    if y1 % 2 == 1 or y2 % 2 == 1:
        print('NO')
    else:
        print('YES')

# 2 solution
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')
