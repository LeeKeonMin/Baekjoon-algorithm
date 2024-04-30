onelist = list()

while True:
    try: 
        n = int(input())
        one = 1
        while True:
            if one % n ==0:
                onelist.append(len(str(one)))
                break
            else:
                one = one*10+1
    except:
        break

for i in onelist:
    print(i)