MAX  = 1000000

# DP 1로 초기화
F = [1]*(MAX+1)

# S: 누적 값 리스트
G = [0]*(MAX+1)

for i in range(2,MAX+1):
    j = 1
    while i*j <= MAX:
        F[i*j] += i
        j += 1

for i in range(1,MAX+1):
    G[i] = G[i-1] + F[i]

n = int(input())
answerlist = list()

for _ in range(n):
    a = int(input())
    answerlist.append(G[a])

for answer in answerlist:
    print(answer)

