a = int(input())
b = int(input())
num1 = b%10
num2 = ((b-num1)/10)%10
num3 = b//100

print(a*num1, a*int(num2),a*num3, a*b, sep='\n')
