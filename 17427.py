#1 시간복잡도 고려 안한 버전.
"""
import math

N = int(input())
sum = 0

for i in range(1,N+1):
    for j in range(1,math.floor(i**(1/2))+1):
        if i % j == 0:
            print(i, j, i//j)
            if j == i//j:
                print('i==i//j')
                sum = sum + j
            else:
                sum = sum + j + i//j
print(sum)
"""

N = int(input())

sum = 0

for i in range(1,N+1):
    sum += (N//i)*i

print(sum)