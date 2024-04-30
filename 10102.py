V = int(input())
votelist = list(input())
A_point = 0
B_point = 0

for i in votelist:
    if i == 'A':
        A_point += 1
    else:
        B_point +=1

if A_point > B_point:
    print('A')
elif A_point == B_point:
    print('Tie')
else:
    print('B')