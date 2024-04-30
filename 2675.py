T = int(input())
repeated_list = list()

for i in range(0,T):
    repeat, str = input().split()
    repeat = int(repeat)
    words = list(str)
    for j in range(0,len(str)):
        words[j] *= repeat

    repeated_list.append(''.join(words))

for i in repeated_list:
    print(i)