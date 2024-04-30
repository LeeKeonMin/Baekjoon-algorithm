year = int(input())
yoon = 1 
yoonx= 0
if year % 4 !=0: #4의배수가 아닌 경우, 윤년이 아님.
    print(yoonx)
elif (year % 4 == 0 and year % 100!=0) or year % 400 ==0: #4의 배수이면서 100의 배수가 아닌경우, 윤년임.
    print(yoon)
else:
    print(yoonx)