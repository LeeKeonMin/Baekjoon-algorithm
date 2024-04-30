N = int (input())
numlist = list(map(int,input().split()))

if N ==1:
    print(max(numlist)**2)

else:
    print(max(numlist)*min(numlist))