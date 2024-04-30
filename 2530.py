hour, min, sec = map(int,input().split())
timer = int(input())
timer_sec = timer%60
timer_min = (timer//60)%60
timer_hour = timer//3600

#print(timer_hour,timer_min,timer_sec)

endsec = sec+timer_sec
endmin = min+timer_min
endhour = hour+timer_hour

Endsec = endsec%60
Endmin  = (endmin + endsec//60)%60
Endhour = (endhour + (endmin+endsec//60)//60)%24


print(Endhour, Endmin, Endsec)
