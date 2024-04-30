# 창영, 상덕
sum_chang = 100
sum_sang = 100

N = int(input())

for i in range(0,N):
    score1, score2 = map(int,input().split())
    if score1 > score2:
        sum_sang -= score1
    elif score1 < score2:
        sum_chang -= score2

print(sum_chang,'\n',sum_sang,sep ='') #공백없이 출력