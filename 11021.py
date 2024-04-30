T = int(input())
numlist = list()
for i in range(0,T):
    temp1, temp2=map(int,input().split())
    numlist.append(temp1+temp2)

enumlist=list(enumerate(numlist))

for index, value in enumerate(numlist):
    message = "Case #{index}: {value}".format(index=index+1, value=value)
    print(message)