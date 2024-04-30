result_list = list()

while True:
    a, b = map(int, input().split())
    if a==0 and b==0:
        break

    if a > b:
        result_list.append('Yes')
    elif a<=b:
        result_list.append('No')
    
for result in result_list:
    print(result)
