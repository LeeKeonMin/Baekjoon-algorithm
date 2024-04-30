N = int(input())
max_score = 0

for i in range(0,N):
        
    a,b,c = map(int,input().split())
    score = 0
    if a == b and b == c:
        score  = 10000 + a*1000
    elif a==b or b==c or a==c:
        if a==b or a==c:
            score = 1000 + 100 * a
        else: 
            score = 1000 + 100 * b
    else:
        score  = max(a,b,c)*100
    
    if score>=max_score:
        max_score = score

print(max_score)

   
