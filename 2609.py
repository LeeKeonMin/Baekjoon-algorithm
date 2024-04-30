a, b = map(int,input().split())
max_divider = 1

for i in range(1,max(a,b)+1):
    if a%i == 0 and b%i ==0:
        max_divider = i

min_gong = (a//max_divider)*(b//max_divider)*max_divider

print(max_divider,'\n',min_gong,sep='')