answer = list()
while True:
    a, b = map(int,input().split())
    
    if a==0 and b==0:
        break

    answer.append(a+b)
    
for x in answer:
    print(x)