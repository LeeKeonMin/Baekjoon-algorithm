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
str_list = list()

while True: 
    M = int(input())
    if not M:
        break
    for _ in range(M//2+1):
        if sosu_hubo_list[_] and sosu_hubo_list[M-_]:
            temp_arr = str(M) + " = " + str(_) + ' + ' + str(M-_)
            str_list.append(temp_arr)
            break
    else:
        print("Goldbach's conjecture is wrong.")

for _ in str_list:
    print(_)