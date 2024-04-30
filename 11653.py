#소인수분해
#정수 N이 주어졌을 때, 소인수분해하는 알고리즘.

N = int(input())
i = 2

while N > 1: 
    if N % i == 0:
        print(i)
        N  = N//i
    elif N % i != 0:
        i += 1

