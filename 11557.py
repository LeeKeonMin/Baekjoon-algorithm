T = int(input())
winner_list = list()

for i in range(0,T):
    N = int(input())
    teamdict = {}

    for j in range(0,N):
        a, b =input().split()
        teamdict[a] = int(b)
    
    max_team = max(teamdict, key = teamdict.get)
    winner_list.append(max_team)


for winner in winner_list:
    print(winner)