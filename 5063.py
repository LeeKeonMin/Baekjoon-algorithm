N = int(input())
advertise = list()

for i in range(0,N):
    r, e, c = map(int,input().split())
    if e-c > r:
        advertise.append('advertise')
    elif e-c == r:
        advertise.append('does not matter')
    else:
        advertise.append('do not advertise')

for x in advertise:
    print(x)