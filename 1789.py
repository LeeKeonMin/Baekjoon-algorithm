# 서로 다른 N개의 자연수의 합이 S라고 한다. 
# S를 알 때, 자연수 N의 최댓값은 얼마일까?

S = int(input())
initial = 0
sum = 0

while sum <= S:
    sum = initial*(initial+1)/2
    initial +=1

print(initial-2)
