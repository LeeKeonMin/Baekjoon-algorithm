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

M,N = map(int,input().split())
input_list = [ i for i in range(M,N+1)]
for _ in range(0, N-M+1):
    if sosu_hubo_list[input_list[_]]:
        print(input_list[_])
