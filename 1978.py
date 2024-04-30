n = 1000000
sosu_hubo_list = [True for i in range(n+1)]

for i in range(2,int(n**(1/2))+1):
    if  sosu_hubo_list[i] == True:
        j = 2
        while i*j <= n:
            sosu_hubo_list[i*j] = False
            j+=1
sosu_hubo_list[0] = False
sosu_hubo_list[1] = False

N = int(input())
input_list = list(map(int,input().split()))
sum = 0
for _ in range(0, N):
    if sosu_hubo_list[input_list[_]]:
        sum+=1

print("sum:",sum)
