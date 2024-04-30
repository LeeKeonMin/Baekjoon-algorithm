# 초등부 올림피아드 문제
# A는 300초, B는 60초, C는 10초
A = B = C = 0


T = int(input())

if T % 10 != 0:
    print(-1)

elif T % 10 ==0:
    if T<= 60:
        if T == 60:
            print(0, 1, 0)
        else:
            print(0, 0, T//10)
    elif T>60 and T<=300:
        if T == 300:
            print(1,0,0)
        else:
            print(0,T//60,(T-(T//60)*60)//10)
    
    else:
        A = T//300
        B = (T - A*300)//60
        C = (T-A*300-B*60)//10
        print(A,B,C)
