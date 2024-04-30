T = int(input())
numlist = list()
Alist = list()
Blist = list()
for i in range(0,T):
    temp1, temp2=map(int,input().split())
    Alist.append(temp1)
    Blist.append(temp2)
    numlist.append(temp1+temp2)

enumlist=list(enumerate(numlist))

for index, value in enumerate(numlist):
    message = "Case #{index}: {A} + {B} = {value}".format(index=index+1, A=Alist[index], B= Blist[index], value=value)
    print(message)