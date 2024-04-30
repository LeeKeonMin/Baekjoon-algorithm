studentlist = list()

for i in range(0,5):
    temp = int(input())
    if temp >= 40:
       studentlist.append(temp)
    else:
        studentlist.append(40)

print(int(sum(studentlist)/len(studentlist)))