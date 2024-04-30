# 최소공배수
T = int(input())
alist = list()

for i in range(0,T):
    a, b = map(int,input().split())
    max_divider = 0 
    for j in range(1,max(a,b)+1):    
        if a%j ==0 and b%j ==0:
            max_divider = j
    alist.append(max_divider*(a//max_divider)*(b//max_divider))

for i in alist:
    print(i)        