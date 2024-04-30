N = int(input())
cute = 0
for i in range(0,N):
    temp = int(input())
    if temp == True:
        cute+=1
    else:
        cute -= 1

if cute >0:
    print('Junhee is cute!')
else: 
    print('Junhee is not cute!')

