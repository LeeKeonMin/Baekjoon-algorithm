x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if x1 == x2:
    new_x = x3 
elif x1 == x3:
    new_x = x2
else:
    new_x = x1

if y1 == y2:
    new_y = y3 
elif y1 == y3:
    new_y = y2
else:
    new_y = y1

print(new_x, new_y)