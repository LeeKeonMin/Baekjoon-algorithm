answer_list = list()

while True:
    n = int(input())
    divider_list = list()
    
    if n == -1:
        break

    for i in range(1,n):
        if n%i == 0:
            divider_list.append(i)
    
    if sum(divider_list) == n:
        divider_list = [str(i) for i in divider_list]
        new_str = ' + '.join(divider_list)
        new_str = str(n) + ' = ' + new_str
        answer_list.append(new_str)
    
    elif sum(divider_list) != n:
        new_str = str(n) + ' is NOT perfect.'
        answer_list.append(new_str)

for answer in answer_list:
    print(answer)

