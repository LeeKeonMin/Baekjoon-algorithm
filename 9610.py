n = int(input())
Q1 = Q2= Q3= Q4 = Axis = 0

for i in range(0,n):
    x1, y1 = map(int,input().split())
    if x1 ==0 or y1 ==0:
        Axis += 1
    elif x1 > 0:  
        if y1>0:
            Q1 += 1
        else:
            Q4 += 1
    else:
        if y1>0:
            Q2 += 1
        else:
            Q3 += 1

print("Q1:", Q1)
print("Q2:", Q2)
print("Q3:", Q3)
print("Q4:", Q4)
print("AXIS:", Axis)
