#첫째 줄에 앨범에 수록된 곡의 개수 A와 평균값 I가 주어진다. 
#(1 ≤ A, I ≤ 100)

A , I = map(int,input().split())

print(A*(I-1)+1)