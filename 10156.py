a, b, c = map(int,input().split())

required_money = a*b
current_money = c

if required_money < current_money:
    yongdon = 0

else: 
    yongdon  = required_money - current_money

print(yongdon)