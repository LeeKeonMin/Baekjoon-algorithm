hour, min = map(int,input().split())
timer = int(input())
timer_min = timer%60
timer_hour = timer//60
#print(timer_hour,timer_min)

Endhour = hour+timer_hour
Endmin = min + timer_min

Endhour = (Endhour + Endmin//60)%24
Endmin = Endmin - (Endmin//60)*60
print(Endhour, Endmin)