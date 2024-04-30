# @ = *3
# % = +5
# # = -7

T = int(input())
numlist = list()

for i in range(0,T):
    str_list = input().split()
    temp = float(str_list[0])
    
    for j in range(1,len(str_list)):
        if str_list[j] == '@':
            temp *= 3
        elif str_list[j] =='%':
            temp += 5
        else:
            temp -= 7 
    
    numlist.append(temp)

for i in numlist:
    print("{:.2f}".format(i))



    